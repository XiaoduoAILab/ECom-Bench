from utils import LLM
from agents import Agent, Runner, ModelSettings, set_default_openai_client, set_default_openai_api, set_tracing_disabled
from openai import AsyncOpenAI
class AgentSDK(LLM):

    # 将配置定义为类变量（缩进与类方法同级）
    DEEPSEEK_V3_CONFIG = {
        "deepseek-v3": {
            "access_key": " ",
            "secret_key": " ",
            "api_key": " ",
            "endpoint_id": " "
        }
    }

    def __init__(self, agent_model: str, verbose=False, mcp_tools=[]):
        # 检查 agent_model 合法性
        if agent_model not in ['qwen', 'deepseek-v3']:
            raise ValueError(f"Unsupported agent_model: {agent_model}")

        # 配置初始化
        if agent_model == 'qwen':
            self.base_url = " "
            self.api_key = " "
            self.model_version = ' '
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
