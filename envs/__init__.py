# Copyright Sierra

from .base import Env
from typing import Optional


def get_env(
    env_name: str,
    user_model: str,
    agent_model:str,
    reward_model:str,
    console_verbose=None,
    task_index: Optional[int] = None,
) -> Env:
    if env_name == "online":
        from .online import MockOnlineEnv

        return MockOnlineEnv(
            user_model=user_model,
            agent_model=agent_model,
            reward_model=reward_model,
            console_verbose=console_verbose,
            task_index=task_index,
        )
        
    elif env_name == "story":
        from .story import MockStoryEnv

        return MockStoryEnv(
            user_model=user_model,
            agent_model=agent_model,
            reward_model=reward_model,
            console_verbose=console_verbose,
            task_index=task_index,
        )
    elif env_name == "recommendation":
        from .recommendation import MockRecommendationEnv
        return MockRecommendationEnv(
            user_model=user_model,
            console_verbose=console_verbose,
            task_index=task_index,
        )
    else:
        raise ValueError(f"Unknown environment: {env_name}")
