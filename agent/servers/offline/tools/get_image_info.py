from typing import List,Dict
from .apis import OnlineLLMApi
from .config import get_config
MULTIMODAL_TYPES = ['doubao-pro', 'qwenvlmax', 'gpt4omini', 'kimi-8k', 'kimi-32k', 'kimi-128k']
    
def get_image_info(data, summarized_query: str, needed_query:str, history_messages: str):
    """
    Returns:
        图片信息的格式化字符串
    """
    if not history_messages or len(history_messages)==0:
        return data, f"参数history_messages有错误，请重新输入。"
    
    input_message = f'''
    "理解对话信息中发送的图片信息和文字信息之间的关系，并给出图片中和当前主要问题有关的描述。'
    请简洁准确地描述图片内容，并遵循以下要求：
    1.忠实描述图片中的主要对象、场景等信息，如果图片描述中有文字，请提取并返回文字内容。
    2.针对每个问题进行相应的回复，并严格遵循格式：
    
    格式如下：
    ### 对图片的描述：
    {{描述的内容}}
    ### 对问题的回答：
    {{回答的内容}}
    ### 对需求的回答：
    {{回答的内容}}
    
    这个是历史对话记录：
    {history_messages}

    这个是用户当前的问题：
    {summarized_query}
    
    这个是对图片内容需求的描述：
    {needed_query}
    '''
    online_llm_api = OnlineLLMApi()
    config = get_config()
    online_llm_api.multimodal_type = config['multimodal']
    messages = [
        {'role': 'user', 'content': input_message}
    ]
    result = online_llm_api.generate_multimodal_response(messages).content
    return data, result