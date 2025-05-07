# Copyright Sierra
import concurrent.futures
import os
import json
import random
import traceback
from math import comb
import multiprocessing
from typing import List, Dict, Any, Tuple
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from rich.progress import Progress
from envs import get_env
from utils import RunConfig, console_verbose

async def run(config: RunConfig) -> List:
    assert config.env in ["online","story","recommendation"]  # , "Only general, recommendation envs are supported"
    random.seed(config.seed)
    time_str = datetime.now().strftime("%m%d%H%M%S")
    ckpt_path = f"{config.log_dir}/{config.agent_strategy}-{config.model.split('/')[-1]}-{config.temperature}_range_{config.start_index}-{config.end_index}_user-{config.user_model}-{config.user_strategy}_{time_str}.json"
    if not os.path.exists(config.log_dir):
        os.makedirs(config.log_dir)
    console_verbose = console_verbose.reset(config.verbose)
    
    env = get_env(
        env_name=config.env,
        user_model=config.user_model,
        agent_model=config.agent_model,
        reward_model=config.reward_model,
        console_verbose=console_verbose
    )
    end_index = (
        len(env.tasks) if config.end_index == -1 else min(config.end_index, len(env.tasks))
    )
    results = []
    lock = multiprocessing.Lock()
    if config.task_ids and len(config.task_ids) > 0:
        console_verbose.print(f"[yellow]Running tasks {config.task_ids} (checkpoint path: {ckpt_path})[/yellow]")  # Running tasks
    else:
        console_verbose.print(
            f"[yellow]Running tasks {config.start_index} to {end_index} (checkpoint path: {ckpt_path})[/yellow]"  # Task range
        )
        
    with Progress() as progress:
        for i in range(config.num_trials):
            if config.task_ids and len(config.task_ids) > 0:
                idxs = config.task_ids
            else:
                idxs = list(range(config.start_index, end_index))
            if config.shuffle:
                random.shuffle(idxs)
            tasks_results = []
            
            async def _run(idx: int) -> Tuple[float, Dict]:
                isolated_env = get_env(
                    env_name=config.env,
                    user_model=config.user_model,
                    agent_model=config.agent_model,
                    reward_model=config.reward_model,
                    console_verbose=console_verbose,
                    task_index=idx
                )
                try:
                    reward, traj = isolated_env.a_run()
                    task_result_str = (
                    f"[green]✅[/green]" if reward > 0 else f"[red]❌[/red]",
                    f"[bold yellow]task_id={idx}[/bold yellow]",
                    # result.info,
                    # "\n[dim]-----------------------------------------------------------------[/dim]"
                )
                except Exception as e:
                    reward, traj = 0.0, [{"error": str(e), "traceback": traceback.format_exc()}]  
                    task_result_str = (
                        f"[green]✅[/green]" if reward > 0 else f"[red]❌[/red]",
                        f"[bold yellow]task_id={idx}[/bold yellow]",
                        # result.info,
                        # "\n[dim]-----------------------------------------------------------------[/dim]"
                    )
                tasks_results.append(task_result_str)
                with lock:
                    data = []
                    if os.path.exists(ckpt_path):
                        with open(ckpt_path, "r") as f:
                            data = json.load(f)
                    with open(ckpt_path, "w") as f:
                        json.dump(data +  [{idx : traj}], f, indent=2)
                return result
            
            task_progress = progress.add_task(f"[yellow]Trial {i + 1} tasks", total=len(idxs))
            reward_results = []
            with ThreadPoolExecutor(max_workers=config.max_concurrency) as executor:
                # 提交所有任务
                future_to_idx = {executor.submit(_run, idx): idx for idx in idxs}
                
                # 处理完成的结果
                for future in concurrent.futures.as_completed(future_to_idx):
                    idx = future_to_idx[future]
                    try:
                        result = future.result()
                        reward_results.append(result)
                        # 更新任务进度
                        progress.update(task_progress, advance=1)
                    except Exception as e:
                        console_verbose.print(f"[red]处理任务 {idx} 时出错: {str(e)}[/red]")

            results.extend(reward_results)
            progress.remove_task(task_progress)
            # 集中打印所有任务结果
            console_verbose.print("\n[bold blue]===== 任务结果摘要 =====[/bold blue]")
            for task_result in tasks_results:
                console_verbose.print(*task_result)


    display_metrics(results)

    with open(ckpt_path, "w") as f:
        json.dump([result.model_dump() for result in results], f, indent=2, ensure_ascii=False)
        console_verbose.print(f"\n[blue]📄 Results saved to {ckpt_path}[/blue]\n")  # Saved result info

    return results



def display_metrics(results: List[float]) -> None:
    
    def is_successful(reward: float) -> bool:
        return 0+1e-6 < reward <= (1 + 1e-6)

    num_trials = len(set([r.trial for r in results]))
    rewards = results
    avg_reward = sum(rewards) / len(rewards)
    # c from https://arxiv.org/pdf/2406.12045
    c_per_task_id: dict[int, int] = {}
    for result in results:
        if result.task_id not in c_per_task_id:
            c_per_task_id[result.task_id] = 1 if is_successful(result.reward) else 0
        else:
            c_per_task_id[result.task_id] += 1 if is_successful(result.reward) else 0
    pass_hat_ks: dict[int, float] = {}
    # 组合数
    # 举例：(5, 3 ✅, 2❌), 一个任务重复5次。 k = 1表示：执行一次的成功概率，k = 2表示：成功执行两次的成功概率
    for k in range(1, num_trials + 1):
        sum_task_pass_hat_k = 0
        for c in c_per_task_id.values():
            sum_task_pass_hat_k += comb(c, k) / comb(num_trials, k)
        pass_hat_ks[k] = sum_task_pass_hat_k / len(c_per_task_id)
    console_verbose.print(f"🏆 Average reward: {avg_reward}")
    console_verbose.print("📈 Pass^k")
    for k, pass_hat_k in pass_hat_ks.items():
        console_verbose.print(f"  k={k}: {pass_hat_k}")

