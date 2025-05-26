# Copyright Sierra
from rich.console import Console
from pydantic import BaseModel
from typing import List, Dict, Optional, Any
from langgraph.prebuilt import create_react_agent
from langchain_community.chat_models import ChatZhipuAI
from langchain_openai import ChatOpenAI
from langchain_openai import AzureChatOpenAI
from abc import ABC, abstractmethod
from datetime import datetime
import os
os.environ["AZURE_OPENAI_API_KEY"] = '0ff535d339e44592b42256a1e2a4cda3'
os.environ["ZHIPUAI_API_KEY"] =  '2d00fac6fbc0408db8bd096b9b704a41.9Hje9rgehzpa22ku'



class Task(BaseModel):
    annotator:str
    user_id: str
    shop_id: str
    platform: str
    instruction: str
    principle: str
    metadata:Optional[Any] = None
    

class Episode(BaseModel):
    time: datetime  # Episode(time="2025-01-03T15:33", instruction="Instruction text")
    instruction: str
    metadata: Optional[Any] = None

class Action(BaseModel):
    function_name:str
    params: Optional[Dict[str, Any]] = None

class EnvRunResult(BaseModel):
    task_id: int
    reward: float
    traj: List[Dict[str, Any]]
    trial: int


class RunConfig(BaseModel):
    agent_model: str
    user_model: str
    reward_model:str 
    num_trials: int 
    env: str
    temperature: float = 0.0
    start_index: int = 0
    end_index: int = -1
    task_ids: Optional[List[int]] = None
    log_dir: str = "results"
    max_concurrency: int = 1
    seed: int = 10
    shuffle: int = 0
    verbose: bool = False




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
                model="glm-4-flash-250414",
                temperature=self.temperature
            )
        elif self.model_name == 'glm-4-plus':
            os.environ["ZHIPUAI_API_KEY"] = '626e93484e6643af9dda2f9deffe803a.rXJLatBAvI7ZwNve'
            self.llm = ChatZhipuAI(
                model="glm-4-plus",
                temperature=self.temperature
            )
        elif self.model_name == 'glm-4-air':
            os.environ["ZHIPUAI_API_KEY"] = '2d00fac6fbc0408db8bd096b9b704a41.9Hje9rgehzpa22ku'
            self.llm = ChatZhipuAI(
                model="glm-4-air-250414",
                temperature=self.temperature
            )
        elif self.model_name == 'glm-z1-air':
            self.llm = ChatZhipuAI(
                model="glm-z1-air",
                temperature=self.temperature
            )
        elif self.model_name == 'deepseek-r1':
            self.llm = ChatOpenAI(
                base_url="https://api.siliconflow.cn/v1/",
                api_key="sk-ebqawkpjzurnbgwyduaxwlziszkyphrqikupmhvmfewlgdcw",
                model="deepseek-ai/DeepSeek-R1",
                temperature=self.temperature
            )
        elif self.model_name == 'deepseek-v3':
            self.llm = ChatOpenAI(
                base_url="https://ark.cn-beijing.volces.com/api/v3",
                api_key="1d5b3a37-e1cc-4617-9a1d-143343600089",
                model="ep-20250207153843-p6tc7",
                temperature=self.temperature
            )
        elif self.model_name == 'gpt-4o':
            self.llm = AzureChatOpenAI(
                azure_endpoint="https://xiaoduoai-ai-data1.openai.azure.com/",
                azure_deployment="gpt-4o",
                openai_api_version="2025-01-01-preview",
                temperature=self.temperature
            )
        elif self.model_name == 'gpt-35':
            self.llm = AzureChatOpenAI(
                azure_endpoint="https://xiaoduoai-ai-data1.openai.azure.com/",
                openai_api_version="2025-01-01-preview",
                azure_deployment="gpt-35-turbo",
                temperature=self.temperature
            )
        elif self.model_name == 'doubao15':
            self.llm = ChatOpenAI(
                base_url="https://ark.cn-beijing.volces.com/api/v3",
                api_key="1d5b3a37-e1cc-4617-9a1d-143343600089",
                model="ep-20250212144301-lf67c",
                temperature=self.temperature
            )
        elif self.model_name == 'qwen':
            self.llm = ChatOpenAI(
                base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
                api_key="sk-d74f4f3190c84ff9a2bf4fee33c8a248",
                model="qwen-max",
                temperature=self.temperature
            )
        elif self.model_name == 'kimi':
            self.llm = ChatOpenAI(
                base_url="https://api.moonshot.cn/v1",
                api_key="sk-7rvYZKZEM9FTo98JD6Y5htTLRCHss0XuX5lDiu6yKsIbyKlJ",
                model="moonshot-v1-32k",
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