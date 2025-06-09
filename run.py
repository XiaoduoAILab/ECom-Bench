# Copyright Sierra

import argparse
from utils import RunConfig
from main import run
import asyncio
from rich.console import Console
console = Console()


def parse_args() -> RunConfig:
    parser = argparse.ArgumentParser()
    parser.add_argument("--num-trials", type=int, default=1)
    parser.add_argument(
        "--env", type=str, choices=["story","recommendation","session", "dialogue"], default="story"
    )
    parser.add_argument(
        "--user-model",
        type=str,
        default="deepseek-v3",
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
    parser.add_argument(
        "--reward-model",
        type=str,
        default="qwen",
        help="The model to use for the reward simulator",
    )
    
    
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="The sampling temperature for the action model",
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
    parser.add_argument("--num_trials", type=int, default=1)
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()
    console.print(f"[green]{args}[/green]")  # Info color
    return RunConfig(
        user_model=args.user_model,
        agent_model=args.agent_model,
        reward_model=args.reward_model,
        user_strategy=args.user_strategy,
        agent_strategy=args.agent_strategy,
        num_trials=args.num_trials,
        env=args.env,
        temperature=args.temperature,
        start_index=args.start_index,
        end_index=args.end_index,
        task_ids=args.task_ids,
        log_dir=args.log_dir,
        max_concurrency=args.max_concurrency,
        seed=args.seed,
        shuffle=args.shuffle,
        verbose=args.verbose,
        # Add any other arguments you want to pass to RunConfig
    )


async def main():
    config = parse_args()
    await run(config)


if __name__ == "__main__":
    asyncio.run(main())
