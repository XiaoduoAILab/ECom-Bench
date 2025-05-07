from .tasks import ALL_TASKS as tasks
from .wiki import WIKI
from envs.base import Env
import random
from user import User
from agent import Agent
import random
from typing import Dict, List, Optional, Dict, Tuple
from langchain_mcp_adapters.client import MultiServerMCPClient
import time
import os

class MockOnlineEnv(Env):
    def __init__(
        self,
        user_model: str = "gpt-4o",
        agent_model: str = "gpt-4o",
        reward_model: str = "gpt-4o",
        task_index: Optional[int] = None,
        console_verbose=None,
    ):
        super().__init__(
            tasks=tasks,
            user_wiki=WIKI,
            user_model=user_model,
            agent_model= agent_model,
            reward_model=reward_model,
            task_index=task_index,
        )
        self.console_verbose = console_verbose
        
    def reset(self, task_index: Optional[int] = None):
        if task_index is None:
            task_index = random.randint(0, len(self.tasks) - 1)
        self.task_index = task_index
        self.task = self.tasks[task_index]
        self.customer = User(self.user_model)
        customer_system_prompt = self.user_wiki.format(demo=self.task.instruction)
        self.customer.load_system_prompt(customer_system_prompt)
        self.service = Agent(self.agent_model)
        self.service.load_system_prompt(self.agent_wiki.format(platform=self.task.platform, shop_id=self.task.shop_id, user_id = self.task.user_id))
    
    async def a_run(self) -> Tuple[float, List[Dict]]:
        self.reset()
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        async with MultiServerMCPClient({
        "service": {
            "command": "python",
            "args": [os.path.join(base_dir,"agent", "server.py")],
            "transport": "stdio",
        }
        }) as client_service:
            self.customer = User(self.user_model)
            self.service = Agent(self.agent_model, mcp_tools=client_service.get_tools())
            self.customer.load_system_prompt(self.user_wiki)
            self.service.load_system_prompt(self.agent_wiki.format(platform=self.task.platform, shop_id=self.task.shop_id, user_id = self.task.user_id))
            self.console_verbose.log(f"\n[bold blue]=== 开始执行任务 ===[/bold blue]")  # Task execution start
            self.console_verbose.log(f"\n[bold green]任务ID: {self.task.task_id}[/bold green]")  # Task ID
            service_response = "亲，需要什么帮助吗？"
            self.session.append({"role": "assistant", "content": service_response})
            for _ in range(30):
                customer_response = self.customer.call(service_response)
                self.console_verbose.log(f"\n[bold magenta]===============Customer response:===============\n{customer_response}[/bold magenta]")
                self.session.append({"role": "user", "content": customer_response})
                if self._is_done(customer_response):
                    break
                start_time = time.time()
                service_response = self.service.call(customer_response)
                end_time = time.time()
                self.elapsed_time.append(round(end_time - start_time, 3))
                self.session.append({"role": "assistant", "content": service_response})
                self.console_verbose.log(f"\n[bold brown]===============Service response:===============\n{service_response}[/bold brown]")           
            self.console_verbose.log(f"\n[bold blue]=== 任务执行完成 ===[/bold blue]")  # Task execution complete
                
        reward = self.calculate_reward(self.session, self.elapsed_time, 1)
        return reward, self.session
