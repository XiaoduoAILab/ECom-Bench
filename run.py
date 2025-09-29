# Copyright Sierra

import argparse
from utils import RunConfig
from main import run
import asyncio
from rich.console import Console
import signal
import sys
console = Console()


def parse_args() -> RunConfig:
    parser = argparse.ArgumentParser()
    parser.add_argument("--num-trials", type=int, default=1)
    parser.add_argument(
        "--env", type=str, choices=["story"], default="story"
    )
    parser.add_argument(
        "--user-model",
        type=str,
        default="qwen",
        help="The model to use for the user simulator",
    )
    parser.add_argument(
        "--user-strategy",
        type=str,
        choices=['human', 'based', 'cot'],
        default='based',
    )
    parser.add_argument(
        "--agent-model",
        type=str,
        default="qwen",
        help="The model to use for the agent simulator",
    )
    parser.add_argument(
        "--agent-strategy",
        type=str,
        choices=['human', 'llm'],
        default='llm',
    )
    parser.add_argument("--start-index", type=int, default=0)
    parser.add_argument("--end-index", type=int, default=-1, help="Run all tasks if -1")
    parser.add_argument("--task-ids", type=int, nargs="+", help="(Optional) run only the tasks with the given IDs")
    parser.add_argument("--log-dir", type=str, default="results")
    parser.add_argument(
        "--max-concurrency",
        type=int,
        default=10,
        help="Number of tasks to run in parallel",
    )
    parser.add_argument("--seed", type=int, default=10)
    parser.add_argument("--shuffle", type=int, default=0)
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument("--max-time",type=int, default=600, help="max time of every task")
    args = parser.parse_args()
    console.print(f"[green]{args}[/green]")  # Info color
    return RunConfig(
        user_model=args.user_model,
        agent_model=args.agent_model,
        user_strategy=args.user_strategy,
        agent_strategy=args.agent_strategy,
        num_trials=args.num_trials,
        env=args.env,
        start_index=args.start_index,
        end_index=args.end_index,
        task_ids=args.task_ids,
        log_dir=args.log_dir,
        max_concurrency=args.max_concurrency,
        seed=args.seed,
        shuffle=args.shuffle,
        verbose=args.verbose,
        max_time=args.max_time,
        # Add any other arguments you want to pass to RunConfig
    )


async def main():
    config = parse_args()
    await run(config)

def signal_handler(sig, frame):
    console.print("[yellow]程序正在退出，清理资源...[/yellow]")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("[yellow]程序被用户中断[/yellow]")
    except Exception as e:
        console.print(f"[red]程序执行错误: {e}[/red]")
    finally:
        # 忽略退出时的事件循环错误
        import warnings
        warnings.filterwarnings("ignore", category=RuntimeWarning, message=".*Event loop is closed.*")
