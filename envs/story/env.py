from .tasks import ALL_TASKS as tasks
from .wiki import WIKI
from envs.base import Env
import shutil
from user import UserCoT as User
from agent import AgentLangChain as Agent
from langchain_core.messages import AIMessage
from agent import OFFLINE_SERVER_DIR, OFFLINE_CACHE_DIR, ActionTools
from typing import Dict, List, Optional, Dict, Tuple
from langchain_mcp_adapters.client import MultiServerMCPClient
import time
import os
import json
import hashlib
class MockStoryEnv(Env):
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
        self.tool_calls = []
        self.data_dir = os.path.join(os.path.dirname(__file__), "data")
        os.makedirs(self.data_dir, mode=0o777,exist_ok=True)

        
    async def a_run(self) -> Tuple[float, List[Dict]]:
        self._create_isolated_data()
        async with MultiServerMCPClient({
        "service": {
            "command": "python",
            "args": [
                os.path.join(OFFLINE_SERVER_DIR, "server.py"),
                "--cache_dir",self.cache_dir
                ],
            "transport": "stdio",
        }
        }) as client_service:
            self.customer = User(self.user_model)
            self.service = Agent(agent_model=self.agent_model, mcp_tools=client_service.get_tools())
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
                self._save_tool_calls(self.service.detail_messages[-1])
                self.elapsed_time.append(round(end_time - start_time, 3))
                self.session.append({"role": "assistant", "content": service_response})
                self.console_verbose.log(f"\n[bold brown]===============Service response:===============\n{service_response}[/bold brown]")           
            self.console_verbose.log(f"\n[bold blue]=== 任务执行完成 ===[/bold blue]")  # Task execution complete
        
        self.original_data = self._load_data(base_dir=self.data_dir)
        self.modified_data = self._load_data(base_dir=self.cache_dir)
        self._remove_isolated_data()
        reward = self.calculate_reward(self.session, self.elapsed_time, 1)
        return reward, self.session
    
    def _is_done(self, message: str) -> bool:
        if ("###STOP###" in message and abs(len(message.strip()) - len("###STOP###")) <= 3) or \
            ("###STOP###" in message and ('祝' in message or '再见' in message or '谢' in message)) or \
            ("转人工" in message):
            return True
        return False
    
    def _create_isolated_data(self):
        # 生成16位随机uuid作为session_id
        import uuid
        self.session_id = str(uuid.uuid4())[:16]
        self.cache_dir = os.path.join(OFFLINE_CACHE_DIR, self.session_id)
        os.makedirs(self.cache_dir, exist_ok=True, mode=0o777)
        os.chmod(self.cache_dir, 0o777)
        # 将data_dir的json文件都复制到cache_dir下
        for file in os.listdir(self.data_dir):
            if file.endswith(".json"):
                shutil.copy(os.path.join(self.data_dir, file), self.cache_dir)
    
    def _remove_isolated_data(self):
        # 删除创建的文件夹
        shutil.rmtree(self.cache_dir)
    
    def _load_data(self, base_dir):
        data = {}
        files = os.listdir(base_dir)
        json_files = [f for f in files if f.endswith('.json')]
        if len(json_files) == 0:
            return data
        else:
            for json_file in json_files:
                file_path = os.path.join(base_dir, json_file)
                file_name = os.path.splitext(json_file)[0]
                with open(file_path, 'r',encoding='utf-8') as f:
                    data[file_name] = json.load(f)
        return data
    
    def calculate_reward(self, session: list[Dict], elapsed_time: List[float], reward: int = 1):
        """
        计算奖励
        :param history: 历史记录
        :param elapsed_time: 消耗的时间
        :return: 奖励结果
        """
        self.console_verbose.log("\n[bold blue]=== 开始计算奖励 ===[/bold blue]")  # Reward calculation start
        reward_time = self.calculate_time_reward(elapsed_time, self.max_time_limit)
        reward_actions = 1 if self.calculate_actions_reward() else 0
        reward_searches = 1 if self.calculate_searches_reward() else 0
        reward_outputs = 1 if self.calculate_outputs_reward() else 0
        self.console_verbose.log(f"\n[bold green]动作奖励[0分 - 1分]: {reward_actions}[/bold green]")
        self.console_verbose.log(f"\n[bold green]搜索奖励[0分 - 1分]: {reward_searches}[/bold green]")
        self.console_verbose.log(f"\n[bold green]输出奖励[0分 - 1分]: {reward_outputs}[/bold green]")
        self.console_verbose.log(f"\n[bold green]时间奖励[0分 - 1分]: {reward_time}[/bold green]")
        reward = 1 * reward_actions * reward_searches * reward_outputs
        self.console_verbose.log(f"\n[bold green]最终计算奖励: {reward}[/bold green]")  # Reward
        return reward
    
    def calculate_actions_reward(self):
        # 计算original_data和modified_data的哈希值
        self._actions_to_tools()
        original_data_hash = hashlib.sha256(json.dumps(self.original_data).encode('utf-8')).hexdigest()
        modified_data_hash = hashlib.sha256(json.dumps(self.modified_data).encode('utf-8')).hexdigest()
        return original_data_hash == modified_data_hash
    
    def _actions_to_tools(self):
        action_tools = ActionTools()
        actions = self.task.metadata.actions
        tools = action_tools.get_available_functions()
        for action in actions:
            for tool in tools:
                if action.name == tool:
                    self.original_data, _ = action_tools.call_function(action.name, data = self.original_data, **action.arguments)
                    break
    
    def _save_tool_calls(self, detail_message):
        for msg in detail_message:
            if type(msg) == AIMessage:
                if msg.additional_kwargs.get("tool_calls"):
                    for tool_call in msg.additional_kwargs["tool_calls"]:
                        self.tool_calls.append(tool_call)
    
    def calculate_searches_reward(self):
        service_data_hash = set()
        for tool_call in self.tool_calls:
            tool_call['function']['arguments'] = json.loads(tool_call['function']['arguments'])
            service_data_hash.add(self._function_to_hash(tool_call['function']))
        search_data_hash = set()
        for search in self.task.metadata.searches:
            search_data_hash.add(self._function_to_hash(search.model_dump()))
        self.console_verbose.log(f"\n[bold red]self.tool_calls:\n{json.dumps([tool_call['function'] for tool_call in self.tool_calls], ensure_ascii=False, indent=2)}[/bold red]")
        # self.console_verbose.log(f"\n[bold red]self.task.metadata.searches:\n{json.dumps([search.model_dump() for search in self.task.metadata.searches], ensure_ascii=False, indent=2)}[/bold red]")
        return search_data_hash.issubset(service_data_hash)
    
    def _function_to_hash(self, function):
        """
        function = {
            "name": "get_product_info",
            "arguments": {
                "product_id": "123456"
            }
        }
        """
        function = json.dumps(function, sort_keys=True, ensure_ascii=False)
        data_hash = hashlib.sha256(function.encode('utf-8')).hexdigest()
        return data_hash
        
    def calculate_outputs_reward(self):
        long_string = "".join([msg['content'] for msg in self.session if msg['role'] == 'assistant'])
        return all([output in long_string for output in self.task.metadata.outputs])
            
    