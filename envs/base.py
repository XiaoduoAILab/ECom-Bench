import random
from typing import Dict, List, Optional, Dict, Tuple
from langchain_mcp_adapters.client import MultiServerMCPClient
from user import UserBased as User
from agent import AgentLangChain as Agent
from wikis import AGENT_WIKI
import time
import os
from utils import Task
from abc import abstractmethod

class Env(object):
    def __init__(
        self,
        tasks: List[Task],
        user_wiki: str,
        agent_wiki: str = AGENT_WIKI,
        user_model: str = "gpt-4o",
        agent_model: str = "gpt-4o",
        max_time_limit: int = 30,
        ratio: float = 1,
        task_index: Optional[int] = None,
    ) -> None:
        self.tasks = tasks
        if task_index is not None:
            self.task_index = task_index
        else:
            self.task_index = random.randint(0, len(tasks)-1)
        self.task = tasks[self.task_index]
        self.user_model = user_model
        self.agent_model = agent_model
        self.max_time_limit = max_time_limit
        self.ratio = ratio
        self.user_wiki = user_wiki
        self.agent_wiki = agent_wiki
        self.session = []
        self.elapsed_time = []
        self.max_turn = 20
        
    async def a_run(self, user_strategy = 'based', agent_strategy = 'llm') -> Tuple[float, List[Dict], Dict]:
        async with MultiServerMCPClient({
        "customer": {
            "command": "python",
            "args": [os.path.join(os.path.dirname(os.path.dirname(__file__)) , "user", "memory.py")],
            "transport": "stdio",
        }
        }) as client_customer:
            # 创建第二个MCP客户端实例（用于AgentB）
            async with MultiServerMCPClient({
                "service": {
                    "command": "python",
                    "args": [os.path.join( os.path.dirname(os.path.dirname(__file__)) ,"agent", "servers","offline","server.py")],
                    "transport": "stdio",
                }
            }) as client_service:
                pass

        detail_reward = {
                'action': 0,
                'search': 0,
                'output': 0,
                'time': 0,
            }
        return reward, self.session, detail_reward
        
    def _is_done(self) -> bool:
        pass 
    
    def calculate_reward(self):
        pass
    
    

