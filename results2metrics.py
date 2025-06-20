import json
import sys
import os
from pydantic import BaseModel
from typing import List, Dict, Any
from math import comb
import json
from collections import defaultdict
from rich.console import Console
from rich.table import Table
console = Console()

class DetailReward(BaseModel):
    action:int
    search:int
    output:int
    time:float
    
class EnvRunResult(BaseModel):
    task_id: int
    reward: float
    traj: List[Dict[str, Any]]
    trial: int
    detail_reward:DetailReward

def load_file(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data

def parse_file(data):
    results = []
    for item in data:
        results.append(
            EnvRunResult(
                task_id = item['task_id'],
                reward = item['reward'],
                traj = item['traj'],
                trial = item['trial'],
                detail_reward = DetailReward(
                    action = item['detail_reward']['action'],
                    search = item['detail_reward']['search'],
                    output = item['detail_reward']['output'],
                    time = item['detail_reward']['time'],
                )
            )
        )
    return results

def gather_file(all_results):
    '''
    all_results: [results_1, results_2, ...]
    '''
    start_traj = 0
    min_traj = 0
    tmp = []
    for index, results in enumerate(all_results):
        for result in results:
            result.trial = result.trial + start_traj
            min_traj = max(min_traj, result.trial)
            tmp.append(result)
        start_traj = min_traj + 1
    return tmp
    

def display_metrics(results: List[EnvRunResult]) -> None:
    
    def is_successful(reward: float) -> bool:
        return 0+1e-6 < reward <= (1 + 1e-6)

    num_trials = len(set([r.trial for r in results]))
    rewards = [r.reward for r in results]
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
    print(f"🏆 Average reward: {avg_reward}")
    print("📈 Pass^k")
    for k, pass_hat_k in pass_hat_ks.items():
        print(f"  k={k}: {pass_hat_k}")
    print("")
    
def display_average(results: List[EnvRunResult]) -> None:
    process_data = defaultdict(list)
    for result in results:
        process_data[result.trial].append(result.reward)
    
    table = Table(title="📊 Trial Average Results", show_header=True, header_style="bold magenta")
    table.add_column("Trial", style="cyan", justify="center")
    table.add_column("Tasks Count", style="green", justify="center")
    table.add_column("Average Reward", style="yellow", justify="center")
    
    for k, v in process_data.items():
        avg_reward = sum(v) / len(v)
        table.add_row(str(k), str(len(v)), f"{avg_reward:.4f}")
    
    console.print(table)
    console.print()

def display_detail(results: List[EnvRunResult]) -> None:
    metric = {
        "action": 0,
        "search": 0,
        "output": 0
    }
    for result in results:
        metric["action"] += result.detail_reward.action
        metric["search"] += result.detail_reward.search
        metric["output"] += result.detail_reward.output
    
    for key in metric:
        metric[key] = 1 - round(metric[key] / len(results), 6)
    
    table = Table(title="🔍 Detailed Fail Rate Analysis", show_header=True, header_style="bold red")
    table.add_column("Component", style="cyan", justify="center")
    table.add_column("Fail Rate", style="red", justify="center")
    table.add_column("Success Rate", style="green", justify="center")
    
    for component, fail_rate in metric.items():
        success_rate = 1 - fail_rate
        table.add_row(
            component.capitalize(),
            f"{fail_rate:.6f} ({fail_rate*100:.2f}%)",
            f"{success_rate:.6f} ({success_rate*100:.2f}%)"
        )
    
    console.print(table)

    
def get_agent_name(files):
    name = []
    for file in files:
        name.append(file.split('_agent-')[1].split('_')[0])
    if all([name[0] == n for n in name]):
        return name[0]
    else:
        raise ValueError("The agent name is not the same")

if __name__ == '__main__':
    
    files = [
        'results/user-qwen_agent-kimi_env-story_range_0--1_0619202640.json',
        'results/user-qwen_agent-kimi_env-story_range_0--1_0620091458.json',
        'results/user-qwen_agent-kimi_env-story_range_0--1_0620095140.json'
        
    ]
    
    model = get_agent_name(files)
    console.print(f"[bold magenta]{'*'*120}")
    print()
    console.print(f"[bold magenta]Model:{model}", justify="center")
    print()
    console.print(f"[bold magenta]{'*'*120}")
    print()
    results = []
    for file in files:
        results.append(
            parse_file(load_file(file))
        )
    all_results = gather_file(results)
    display_metrics(all_results)
    display_average(all_results)
    display_detail(all_results)
    
    