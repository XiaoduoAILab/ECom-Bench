from utils import LLM

class AgentLangChain(LLM):
    def __init__(self, agent_model:str, verbose=False, mcp_tools= []):
        super().__init__(model_name=agent_model, verbose=verbose, mcp_tools=mcp_tools)
        self.agent_model = super()._initiate_agent()
        self.detail_messages = []
    
    
    def load_system_prompt(self, system_prompt):
        self.messages.append({"role": "system", "content": system_prompt})
    
    
    async def call(self, message:str) -> str:
        self.messages.append({"role": "user", "content": message})
        responses = await self.agent_model.ainvoke(
            input = {
                "messages": self.messages
            },
            debug=self.verbose
        )
        self.detail_messages.append(responses["messages"])
        self.messages.append({"role": "assistant", "content": responses["messages"][-1].content})
        # print(self.detail_messages)
        return responses["messages"][-1].content
    
    
    



from agents import Agent, Runner, ModelSettings, set_default_openai_client, set_default_openai_api, set_tracing_disabled
from openai import AsyncOpenAI
class AgentSDK(LLM):

    # 将配置定义为类变量（缩进与类方法同级）
    DEEPSEEK_V3_CONFIG = {
        "deepseek-v3": {
            "access_key": "AKLTZjNmZmE3NTY3NzJhNGViZTlmM2FkMmU5YjAwNjZhZDQ",
            "secret_key": "T0dRMU1UVXhNelV4TVRsaE5EaGxORGxoTW1OaE5ERTNZVGt3TldJME9Eaw==",
            "api_key": "1d5b3a37-e1cc-4617-9a1d-143343600089",
            "endpoint_id": "ep-20250207153843-p6tc7"
        }
    }

    def __init__(self, agent_model: str, verbose=False, mcp_tools=[]):
        # 检查 agent_model 合法性
        if agent_model not in ['qwen', 'deepseek-v3']:
            raise ValueError(f"Unsupported agent_model: {agent_model}")

        # 配置初始化
        if agent_model == 'qwen':
            self.base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
            self.api_key = "sk-d74f4f3190c84ff9a2bf4fee33c8a248"
            self.model_version = 'qwen-max'
        else:
            self.base_url = "https://ark.cn-beijing.volces.com/api/v3"
            self.api_key = self.DEEPSEEK_V3_CONFIG["deepseek-v3"]['api_key']  # 使用类名引用类变量
            self.model_version = self.DEEPSEEK_V3_CONFIG["deepseek-v3"]['endpoint_id']        
        self.llm_client = AsyncOpenAI(base_url=self.base_url, api_key=self.api_key)
        set_default_openai_client(self.llm_client)
        set_default_openai_api("chat_completions")
        set_tracing_disabled(True)
        self.verbose = verbose
        self.mcp_servers = mcp_tools
        self.messages = []
        self.detail_messages = []
        self.temperature = 0.5 
        
        
        self.agent_model =  Agent(
            name="金牌电商客服助手",
            model=self.model_version,
            mcp_servers=[self.mcp_servers],
            model_settings=ModelSettings(temperature=self.temperature, max_tokens=256)
        )


        
    def load_system_prompt(self, system_prompt):
        self.messages.append({"role": "system", "content": system_prompt})  
        
    async def call(self, message:str) -> str:
        self.messages.append({"role": "user", "content": message})
        responses = await Runner.run(
            self.agent_model,
            input=self.messages,
        )
        self.detail_messages.append(responses.to_input_list())
        self.messages.append({"role": "assistant", "content": responses.final_output})
        return responses.final_output