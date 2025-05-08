import random
from typing import Any, Dict, List, Optional, Dict, Tuple
from langchain_mcp_adapters.client import MultiServerMCPClient
from user import User
from agent import Agent
from .reward import Reward
from wikis import AGENT_WIKI
import time
import os
from utils import Task


class Env(object):
    def __init__(
        self,
        tasks: List[Task],
        user_wiki: str,
        agent_wiki: str = AGENT_WIKI,
        user_model: str = "gpt-4o",
        agent_model: str = "gpt-4o",
        reward_model: str = "gpt-4o",
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
        self.reward_model = reward_model
        self.max_time_limit = max_time_limit
        self.ratio = ratio
        self.user_wiki = user_wiki
        self.agent_wiki = agent_wiki
        self.session = []
        self.elapsed_time = []
        
    def run(self) -> Tuple[float, List[Dict]]:
        self.customer = User(self.user_model)
        self.service = Agent(self.agent_model)
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
        
    async def a_run(self) -> Tuple[float, List[Dict]]:
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
                    "args": [os.path.join( os.path.dirname(os.path.dirname(__file__)) ,"agent", "server.py")],
                    "transport": "stdio",
                }
            }) as client_service:
                self.customer = User(self.user_model, mcp_tools=client_customer.get_tools())
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
        
    def _is_done(self, message: str) -> bool:
        return "###STOP###" in message and abs(len(message.strip()) - len("###STOP###")) <= 3    
    
    def calculate_reward(self, session: list[Dict], elapsed_time: List[float], reward: int = 1):
        """
        计算奖励
        :param history: 历史记录
        :param elapsed_time: 消耗的时间
        :return: 奖励结果
        """
        self.console_verbose.log("\n[bold blue]=== 开始计算奖励 ===[/bold blue]")  # Reward calculation start
        history = []
        for msg in session:
            if msg['role'] == 'user':
                history.append(f"顾客：{msg['content']}\n")
            elif msg['role'] == 'assistant':
                history.append(f"客服：{msg['content']}\n")
        if len(history) == 0 or len(elapsed_time) == 0:
            return 0.0
        principle = self.task.principle
        self.console_verbose.log(f"\n[bold green]=========奖励模型打分规则=========\n: {principle}[/bold green]")  # Reward model scoring rules
        # 计算内容奖励
        self.reward = Reward(self.reward_model)
        reward_score, reward_content = self.reward.call(rules=principle, history=history)
        # 计算时间奖励
        reward_time = self.calculate_time_reward(elapsed_time, self.max_time_limit)
        self.console_verbose.log(f"\n[gradient(90, red, purple)]=========奖励模型打分回复=========\n{reward_content}[/gradient(90, red, purple)]")
        self.console_verbose.log(f"\n[bold green]内容奖励[0分 - 1分]: {reward_score}[/bold green]")  # Content reward
        self.console_verbose.log(f"\n[bold green]时间奖励[0分 - 1分]: {reward_time}[/bold green]")
        reward = reward * ( (self.ratio * reward_score) + ((1 - self.ratio) * reward_time) )
        self.console_verbose.log(f"\n[bold green]最终计算奖励: {reward}[/bold green]")  # Reward
        return reward
    
    def calculate_time_reward(self, elapsed_time: List[float], max_limit:int):
        """
        计算时间奖励
        :param elapsed_time: 消耗的时间
        :param max_limit: 最大限制
        :param ratio: 比例
        :return: 奖励结果
        """
        avg_time = sum(elapsed_time) / len(elapsed_time)
        if avg_time <= 0:
            raise ValueError("avg_time must be greater than 0")
        elif avg_time > max_limit:
            return 0.0
        else:
            # 使用反比例函数生成平滑曲线，确保在0到0.5之间
            return round((max_limit - avg_time) / (max_limit + avg_time), 3)
    

