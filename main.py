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
import traceback
import asyncio  # 添加asyncio导入，用于处理协程

async def run(config: RunConfig) -> List:
    assert config.env in ["online","story","recommendation"]  
    random.seed(config.seed)
    time_str = datetime.now().strftime("%m%d%H%M%S")
    ckpt_path = f"{config.log_dir}/user-{config.user_model}_agent-{config.agent_model}_reward-{config.reward_model}_range_{config.start_index}-{config.end_index}_{time_str}.json"
    if not os.path.exists(config.log_dir):
        os.makedirs(config.log_dir)
    console_verbose.reset(config.verbose)
    
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
    all_reward_results = [] # num_trials 的结果
    all_tasks_results = [] # num_trials 的结果
    
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
                
            # 修改：将异步函数改为普通函数，内部使用await处理异步调用
            def _run(idx: int) -> Tuple[float, Dict]:
                isolated_env = get_env(
                    env_name=config.env,
                    user_model=config.user_model,
                    agent_model=config.agent_model,
                    reward_model=config.reward_model,
                    console_verbose=console_verbose,
                    task_index=idx
                )
                try:
                    # 创建事件循环并运行协程
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    reward, traj = loop.run_until_complete(isolated_env.a_run())
                    loop.close()
                    
                    task_result_str = (
                        f"✅" if reward > 0 else f"❌",
                        f"task_id={idx}",
                        # result.info,
                        # "\n[dim]-----------------------------------------------------------------[/dim]"
                    )
                except Exception as e:
                    reward, traj = 0.0, [{"error": str(e), "traceback": traceback.format_exc()}]
                    
                    console_verbose.print(f"[red]\n处理任务 {idx} 时出错: {str(e)}[/red]")
                    console_verbose.print(traceback.format_exc())  # 这会打印完整的堆栈跟踪  
                    task_result_str = (
                        f"✅" if reward > 0 else f"❌",
                        f"task_id={idx}",
                        # result.info,
                        # "\n[dim]-----------------------------------------------------------------[/dim]"
                    )
                with lock:
                    data = []
                    if os.path.exists(ckpt_path):
                        with open(ckpt_path, "r") as f:
                            data = json.load(f)
                    with open(ckpt_path, "w") as f:
                        json.dump(data +  [{idx : traj}], f, indent=2, ensure_ascii=False)
                return (reward, task_result_str)
            
            task_progress = progress.add_task(f"[yellow]Trial {i + 1} tasks", total=len(idxs))
            reward_results = [] # 每个trial的结果, rewards
            tasks_results = [] # 每个trial的结果
            with ThreadPoolExecutor(max_workers=config.max_concurrency) as executor:
                # 提交所有任务
                future_to_idx = {executor.submit(_run, idx): idx for idx in idxs}
                
                # 处理完成的结果
                for future in concurrent.futures.as_completed(future_to_idx):
                    idx = future_to_idx[future]
                    try:
                        result = future.result()  # 这里不再是协程，而是直接获取结果
                        reward_results.append(result[0])
                        tasks_results.append(result[1])
                        # 更新任务进度
                        progress.update(task_progress, advance=1)
                    except Exception as e:
                        console_verbose.print(f"[red]\n处理任务 {idx} 时出错: {str(e)}[/red]")
                        console_verbose.print(traceback.format_exc())  # 这会打印完整的堆栈跟踪

            all_reward_results.extend(reward_results)
            all_tasks_results.append({"num_trial": i+1, "results": tasks_results})
            progress.remove_task(task_progress)
            # 集中打印所有任务结果
            console_verbose.print("\n[bold blue]===== 任务结果摘要 =====[/bold blue]")
            for results in all_tasks_results:  # 修复：移除解包，直接使用结果对象
                console_verbose.print(f"[bold blue]Trial {results['num_trial']}[/bold blue]：\n")  # 修复：使用字典访问
                batch_size = 10
                for i in range(0, len(results['results']), batch_size):  # 修复：访问results字典中的'results'列表
                    batch_results = results['results'][i:i+batch_size]
                    batch_results = [' '.join(r) for r in batch_results]
                    console_verbose.print(f'[bold blue] {'  '.join(batch_results)}')
                console_verbose.print("\n[bold blue]-------------------[/bold blue]\n")


    # display_metrics(all_reward_results)

    with open(ckpt_path, "w") as f:
        json.dump([reward for reward in all_reward_results], f, indent=2, ensure_ascii=False)
        console_verbose.print(f"\n[blue]📄 Results saved to {ckpt_path}[/blue]\n")  # Saved result info

    return all_reward_results  # 修复：应该返回结果列表而不是未定义的变量



def display_metrics(results: List[float]) -> None:
    if len(results) == 0:
        return None
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

