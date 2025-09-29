from .models import AzureOpenAIClient, QwenModelClient, DoubaoModelClient, Doubao1_5ModelClient, DeepseekV3ModelClient, MultimodalModelClient
from .console import console_model
MODEL_TYPES = ['gpt35', 'gpt4o', 'qwen', 'doubao', 'doubao15', 'deepseek_v3']
MULTIMODAL_TYPES = ['doubao-pro', 'qwenvlmax', 'gpt4omini', 'kimi-8k', 'kimi-32k', 'kimi-128k']


class OnlineLLMApi:
    multimodal_type = 'gpt4omini'
    def __init__(self):
        self.console = console_model

        # Initialize all model clients
        self.azure_client = AzureOpenAIClient(
            api_base=" ",
            api_key=" ",
            api_version=" ",
            console=self.console
        )
        self.qwen_client = QwenModelClient(
            api_key=" ",
            base_url=" ",
            console=self.console
        )
        self.doubao_client = DoubaoModelClient(
            api_key=" ",
            base_url=" ",
            endpoint_id=" ",
            console=self.console
        )
        self.doubao_1_5_client = Doubao1_5ModelClient(
            # api_key="your_doubao_1_5_api_key",
            api_key = " ",
            base_url=" ",
            endpoint_id = " ",
            console=self.console
            # endpoint_id="your_endpoint_id",
        )
        self.deepseek_client = DeepseekV3ModelClient(
            # api_key="your_deepseek_api_key",
            api_key=" ",
            base_url=" ",
            endpoint_id=" ",
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
