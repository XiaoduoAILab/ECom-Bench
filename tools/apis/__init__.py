from .models import AzureOpenAIClient, QwenModelClient, DoubaoModelClient, Doubao1_5ModelClient, DeepseekV3ModelClient, MultimodalModelClient
from rich.console import Console
from langchain_community.chat_models import ChatZhipuAI
from langchain_openai import ChatOpenAI
from langchain_openai import AzureChatOpenAI
import os
os.environ["AZURE_OPENAI_API_KEY"] = '0ff535d339e44592b42256a1e2a4cda3'
os.environ["ZHIPUAI_API_KEY"] =  '2d00fac6fbc0408db8bd096b9b704a41.9Hje9rgehzpa22ku'


MODEL_TYPES = ['gpt35', 'gpt4o', 'qwen', 'doubao', 'doubao15', 'deepseek_v3']
MULTIMODAL_TYPES = ['doubao-pro', 'qwenvlmax', 'gpt4omini', 'kimi-8k', 'kimi-32k', 'kimi-128k']

class ModelLogger:
    def __init__(self, verbose=False):
        self.console = Console()
        self.verbose = verbose  # 默认不启用日志
    
    def print(self, *args):
        self.console.print(*args)
        
    def log(self, *args):
        if self.verbose:
            self.console.log(*args)
        else:
            # 如果没有启用日志，什么都不做
            pass
    
class OnlineLLMApi:
    multimodal_type = 'gpt4omini'
    
    def __init__(self, verbose=False):
        self.console = ModelLogger(verbose=verbose)

        # Initialize all model clients
        self.azure_client = AzureOpenAIClient(
            api_base="https://xiaoduoai-ai-data1.openai.azure.com/",
            api_key="0ff535d339e44592b42256a1e2a4cda3",
            api_version="2025-01-01-preview",
            console=self.console
        )
        self.qwen_client = QwenModelClient(
            api_key="sk-d74f4f3190c84ff9a2bf4fee33c8a248",
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            console=self.console
        )
        self.doubao_client = DoubaoModelClient(
            api_key="1d5b3a37-e1cc-4617-9a1d-143343600089",
            base_url="https://ark.cn-beijing.volces.com/api/v3",
            endpoint_id="ep-20240520050246-ctznf",
            console=self.console
        )
        self.doubao_1_5_client = Doubao1_5ModelClient(
            # api_key="your_doubao_1_5_api_key",
            api_key = "1d5b3a37-e1cc-4617-9a1d-143343600089",
            base_url="https://ark.cn-beijing.volces.com/api/v3",
            endpoint_id = "ep-20250212144301-lf67c",
            console=self.console
            # endpoint_id="your_endpoint_id",
        )
        self.deepseek_client = DeepseekV3ModelClient(
            # api_key="your_deepseek_api_key",
            api_key="1d5b3a37-e1cc-4617-9a1d-143343600089",
            base_url="https://ark.cn-beijing.volces.com/api/v3",
            endpoint_id="ep-20250207153843-p6tc7",
            console=self.console
            # endpoint_id="your_endpoint_id"
        )
        self.multimodal_client = MultimodalModelClient(console=self.console)

    def generate_response(self, model_type, messages, tools=None):
        if model_type == 'gpt35':
            response = self.azure_client.create_response("gpt-35-turbo", messages, tools)
        elif model_type == 'gpt4o':
            response = self.azure_client.create_response("gpt-4o", messages, tools)
        elif model_type == 'qwen':
            response = self.qwen_client.create_response(messages, tools)
        elif model_type == 'doubao':
            response = self.doubao_client.create_response(messages, tools)
        elif model_type == 'doubao15':
            response = self.doubao_1_5_client.create_response(messages, tools)
        elif model_type == 'deepseek_v3':
            response = self.deepseek_client.create_response(messages, tools)
        elif model_type in ['kimi-8k', 'kimi-32k', 'kimi-128k', 'qwenvlmax', 'doubao-pro']:
            response = self.multimodal_client.create_response(messages, model_type, tools)
        else:
            self.console.log("Model type not recognized.")
            return "Model type not recognized."
        return response
    
    def generate_multimodal_response(self, messages, tools=None):
        if self.multimodal_type in MULTIMODAL_TYPES:
            response = self.multimodal_client.create_response(messages, self.multimodal_type, tools)
        else:
            self.console.log("Multimodal type not recognized.")
            return "Model type not recognized."

        return response
    
    
def _initiate_user(user):
    if user == 'glm-4-flash':
        LLM = ChatZhipuAI(
            model="glm-4-flash-250414",
            temperature=0.3
            )
    elif user == 'glm-4-plus':
        os.environ["ZHIPUAI_API_KEY"] = '626e93484e6643af9dda2f9deffe803a.rXJLatBAvI7ZwNve'
        LLM = ChatZhipuAI(
            model="glm-4-plus",
            temperature=0.3
            )
    elif user == 'glm-4-air':
        os.environ["ZHIPUAI_API_KEY"] = '2d00fac6fbc0408db8bd096b9b704a41.9Hje9rgehzpa22ku' # 2d00fac6fbc0408db8bd096b9b704a41.9Hje9rgehzpa22ku
        LLM = ChatZhipuAI(
            model="glm-4-air-250414",
            temperature=0.3
            )
    elif user == 'glm-z1-air':
        LLM = ChatZhipuAI(
            model="glm-z1-air",
            temperature=0.3
            )
    elif user == 'deepseek-r1':
        LLM = ChatOpenAI(
        base_url="https://api.siliconflow.cn/v1/",
        api_key="sk-ebqawkpjzurnbgwyduaxwlziszkyphrqikupmhvmfewlgdcw",    # app_key
        model="deepseek-ai/DeepSeek-R1",   # 模型名称
    )
    elif user == 'deepseek-v3':
    #     LLM = ChatOpenAI(
    #     base_url="https://api.siliconflow.cn/v1/",
    #     api_key="sk-ebqawkpjzurnbgwyduaxwlziszkyphrqikupmhvmfewlgdcw",    # app_key
    #     model="deepseek-ai/DeepSeek-V3",   # 模型名称
    # )
        LLM = ChatOpenAI(
        base_url="https://ark.cn-beijing.volces.com/api/v3",
        api_key="1d5b3a37-e1cc-4617-9a1d-143343600089",    # app_key
        model="ep-20250207153843-p6tc7",   # 模型名称
    )
    elif user == 'gpt-4o':
        LLM = AzureChatOpenAI(
        azure_endpoint="https://xiaoduoai-ai-data1.openai.azure.com/",
        azure_deployment = "gpt-4o",
        openai_api_version="2025-01-01-preview",
    )
    elif user == 'gpt-35':
        LLM = AzureChatOpenAI(
        azure_endpoint="https://xiaoduoai-ai-data1.openai.azure.com/",
        openai_api_version="2025-01-01-preview",
        azure_deployment = "gpt-35-turbo",
    )
    elif user == 'doubao15':
        LLM = ChatOpenAI(
        base_url="https://ark.cn-beijing.volces.com/api/v3",
        api_key="1d5b3a37-e1cc-4617-9a1d-143343600089",    # app_key
        model="ep-20250212144301-lf67c",   # 模型名称
    )
    elif user == 'qwen':
        LLM = ChatOpenAI(
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        api_key="sk-d74f4f3190c84ff9a2bf4fee33c8a248",    # app_key
        model="qwen-max",   # 模型名称
    )
    elif user == 'gpt-4o-vino':
        LLM = ChatOpenAI(
        base_url="https://sk.vinoai.net/v1",
        api_key="sk-W2fT6Mn6iGwWnNCWD274Ec5c8eE64c648f5bB8E5A5D8069f",    # app_key
        model="gpt-4o",   # 模型名称
        )
    elif user == 'gpt-35-vino':
        LLM = ChatOpenAI(
        base_url="https://sk.vinoai.net/v1",
        api_key="sk-W2fT6Mn6iGwWnNCWD274Ec5c8eE64c648f5bB8E5A5D8069f",    # app_key
        model="gpt-3.5-turbo",   # 模型名称
        )
    elif user == 'kimi':
        LLM = ChatOpenAI(
        base_url="https://api.moonshot.cn/v1",
        api_key="sk-7rvYZKZEM9FTo98JD6Y5htTLRCHss0XuX5lDiu6yKsIbyKlJ",    # app_key
        model="moonshot-v1-32k",   # 模型名称
    )
    else:
        raise ValueError(f"Unsupported user: {user}")
    return LLM

if __name__ == "__main__":
    api = OnlineLLMApi()
    messages = [{'role': 'system', 'content': f'''\n                    
"你是一个高级的电商客服，你要理解对话信息中发送的图片信息和文字信息之间的关系，并给出图片中和当前主要问题有关的描述。\'\n              
请简洁准确地描述图片内容，并遵循以下要求：\n                    
1.：忠实描述图片中的主要对象、场景等信息，如果图片描述中有文字，请提取并返回文字内容。\n                    2： 
描述内容尽量只输出和用户主要问题相关的信息，简介明了不超过100个字"\n                   '''}, {'role': 'user', 'content':f''' 
'https://chat-img.pddugc.com/chat-pic-mall-user-v1/2025-04-06/7a963da6-a2e4-4340-aa88-10c008c6fb9c.jpeg 
这图片上显示的尺寸好像和你们说的不一样啊。'''}]
    response = api.generate_multimodal_response(messages)
    print(response)
