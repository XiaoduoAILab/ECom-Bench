from .tasks import ALL_TASKS as tasks
from .wiki import WIKI
from envs.base import Env
from langchain_mcp_adapters.client import MultiServerMCPClient
from user import UserBased as User
from agent import AgentLangChain as Agent
from agent import ONLINE_SERVER_DIR
from typing import Dict, List, Optional, Dict, Tuple
import time
import os

class MockDialogueEnv(Env):
    
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
        
    async def a_run(self, user_strategy = 'based', agent_strategy = 'llm') -> Tuple[float, List[Dict]]:
        async with MultiServerMCPClient({
        "service": {
            "command": "python",
            "args": [
                os.path.join(ONLINE_SERVER_DIR, "server.py"),
                ],
            "transport": "stdio",
        }
        }) as client_service:
            self.customer = User(self.user_model)
            self.service = Agent(self.agent_model, mcp_tools=client_service.get_tools())
            self.customer.load_system_prompt(self.user_wiki.format(instruction=self.task.instruction))
            self.service.load_system_prompt(self.agent_wiki.format(platform=self.task.platform, shop_id=self.task.shop_id, user_id = self.task.user_id))
            self.console_verbose.log(f"\n[bold blue]=== 开始执行任务 ===[/bold blue]")  # Task execution start
            self.console_verbose.log(f"\n[bold green]任务ID: {self.task_index}[/bold green]")  # Task ID
            service_response = "亲，需要什么帮助吗？"
            self.session.append({"role": "assistant", "content": service_response})
            for _ in range(30):
                customer_response = await self.customer.call(service_response)
                self.console_verbose.log(f"\n[bold magenta]===============Customer response:===============\n{customer_response}[/bold magenta]")
                self.session.append({"role": "user", "content": customer_response})
                if self._is_done(customer_response):
                    break
                start_time = time.time()
                service_response = await self.service.call(customer_response)
                end_time = time.time()
                self.elapsed_time.append(round(end_time - start_time, 3))
                self.session.append({"role": "assistant", "content": service_response})
                self.console_verbose.log(f"\n[bold brown]===============Service response:===============\n{service_response}[/bold brown]")           
            self.console_verbose.log(f"\n[bold blue]=== 任务执行完成 ===[/bold blue]")  # Task execution complete
                
        reward = self.calculate_reward(self.session, self.elapsed_time, 1)
        return reward, self.session
    
    def _is_done(self, message: str) -> bool:
        if ("###STOP###" in message and abs(len(message.strip()) - len("###STOP###")) <= 3) or \
            ("###STOP###" in message and ('祝' in message or '再见' in message or '谢' in message)):
            return True
        return False

