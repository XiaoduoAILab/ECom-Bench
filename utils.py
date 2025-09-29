from rich.console import Console
from rich.table import Table
import json
from pydantic import BaseModel
from typing import List, Dict, Optional, Any
from langgraph.prebuilt import create_react_agent
from langchain_community.chat_models import ChatZhipuAI
from langchain_openai import ChatOpenAI
from langchain_openai import AzureChatOpenAI
from abc import ABC, abstractmethod
from datetime import datetime
import os
os.environ["AZURE_OPENAI_API_KEY"] = ' '
os.environ["ZHIPUAI_API_KEY"] =  ' '


class ProductInfo(BaseModel):
    product_id:str
    quantity: int
class Task(BaseModel):
    annotator:str
    user_id: str
    shop_id: str
    platform: str
    instruction: str
    metadata:Optional[Any] = None
    
class Search(BaseModel):
    name:str
    arguments: Optional[Dict[str, Any]] = None
    
class Action(BaseModel):
    name:str
    arguments: Optional[Dict[str, Any]] = None
    
class Validation(BaseModel):
    outputs: List[str] = []
    actions: List[Action] = []
    searches: List[Search] = [] 

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

class Episode(BaseModel):
    time: datetime  # Episode(time="2025-01-03T15:33", instruction="Instruction text")
    instruction: str
    metadata: Optional[Any] = None
class RunConfig(BaseModel):
    agent_model: str
    user_model: str
    num_trials: int 
    env: str
    user_strategy: str
    agent_strategy: str
    start_index: int = 0
    end_index: int = -1
    task_ids: Optional[List[int]] = None
    log_dir: str = "results"
    max_concurrency: int = 1
    seed: int = 10
    shuffle: int = 0
    verbose: bool = False
    max_time: int = 300




class RunLogger:
    def __init__(self, verbose=False):
        self.console = Console()
        self.verbose = verbose  # 默认不启用日志
    def reset(self, verbose):
        self.verbose = verbose
    def print(self, *args):
        self.console.print(*args)
    def log(self, *args):
        if self.verbose:
            self.console.log(*args)
        else:
            # 如果没有启用日志，什么都不做
            pass
    
    def log_table(self, data_list, title="Table", name_column="Name", args_column="Arguments"):
        """输出表格格式的数据
        
        Args:
            data_list: 包含字典的列表，每个字典应有'name'和'arguments'键
            title: 表格标题
            name_column: 名称列的标题
            args_column: 参数列的标题
        """
        if self.verbose:
            print("\n\n")
            table = Table(
                title=title, 
                show_header=True, 
                header_style="bold magenta",
                show_lines=True,  # 添加这个参数来显示行分隔线
            )
            table.add_column(name_column, style="cyan", justify="left")
            table.add_column(args_column, style="yellow", justify="left")
            
            for item in data_list:
                name = item.get('name', 'N/A')
                arguments = item.get('arguments', {})
                # 将arguments格式化为JSON字符串，但限制长度以保持表格美观
                args_str = json.dumps(arguments, ensure_ascii=False, indent=2)
                table.add_row(name, args_str)
            
            self.console.print(table)
        else:
            # 如果没有启用日志，什么都不做
            pass

console_verbose = RunLogger()

class LLM(ABC): 
    def __init__(self, model_name:str, verbose:bool=False, mcp_tools=[], temperature=0.3):
        self.model_name = model_name
        self.verbose = verbose
        self.mcp_tools = mcp_tools
        self.llm = None  # 初始化llm属性
        self.messages = []
        self.temperature = temperature
        self._initiate_llm()  # 初始化时直接创建LLM实例
    
    def _initiate_llm(self):
        if self.model_name == 'glm-4-flash':
            self.llm = ChatZhipuAI(
                model = " ",
                temperature = self.temperature
            )
        elif self.model_name == 'glm-4-plus':
            os.environ["ZHIPUAI_API_KEY"] = ' '
            self.llm = ChatZhipuAI(
                model=" ",
                temperature=self.temperature
            )
        elif self.model_name == 'glm-4-air':
            os.environ["ZHIPUAI_API_KEY"] = ' '
            self.llm = ChatZhipuAI(
                model=" ",
                temperature=self.temperature
            )
        elif self.model_name == 'glm-z1-air':
            self.llm = ChatZhipuAI(
                model=" ",
                temperature=self.temperature
            )
            
        elif self.model_name == 'glm-4-air-250414':
            os.environ["ZHIPUAI_API_KEY"] = ' '
            self.llm = ChatZhipuAI(
                model=" ",
                temperature=self.temperature
            )
        elif self.model_name == 'deepseek-r1':
            self.llm = ChatOpenAI(
                base_url=" ",
                api_key=" ",
                model=" ",
                temperature=self.temperature
            )
        elif self.model_name == 'deepseek-v3':
            self.llm = ChatOpenAI(
                base_url=" ",
                api_key=" ",
                model=" ",
                temperature=self.temperature
            )
        elif self.model_name == 'gpt-4o':
            self.llm = AzureChatOpenAI(
                azure_endpoint=" ",
                azure_deployment=" ",
                openai_api_version=" ",
                temperature=self.temperature
            )
        elif self.model_name == 'gpt-35':
            self.llm = AzureChatOpenAI(
                azure_endpoint=" ",
                openai_api_version=" ",
                azure_deployment=" ",
                temperature=self.temperature
            )
        elif self.model_name == 'doubao15':
            self.llm = ChatOpenAI(
                base_url=" ",
                api_key=" ",
                model=" ",
                temperature=self.temperature
            )
        elif self.model_name == 'qwen':
            self.llm = ChatOpenAI(
                base_url=" ",
                api_key=" ",
                model=" ",
                temperature=self.temperature
            )
        elif self.model_name == 'kimi':
            self.llm = ChatOpenAI(
                base_url=" ",
                api_key=" ",
                model=" ",
                temperature=self.temperature
            )
        elif self.model_name == 'qwenvlmax':
            self.llm = ChatOpenAI(
                base_url=" ",
                api_key=" ",
                model=" ",
                temperature=self.temperature
            )
        else:
            raise ValueError(f"Unsupported model: {self.model_name}")
                
    def _initiate_agent(self):
        return create_react_agent(
            self.llm,  # 直接使用已初始化的self.llm
            self.mcp_tools
        )
    
    @abstractmethod
    def load_system_prompt(self, system_prompt):
        """初始化系统提示词"""
        pass
    
    @abstractmethod
    def call(self, message: str) -> str:
        """子类必须实现的消息处理方法
        
        Args:
            message: 输入的消息文本
            
        Returns:
            返回处理后的消息文本
        """
        pass
