from typing import List,Dict
from .apis import OnlineLLMApi
MULTIMODAL_TYPES = ['doubao-pro', 'qwenvlmax', 'gpt4omini', 'kimi-8k', 'kimi-32k', 'kimi-128k']
    
def get_image_info(summarized_query: str, history_messages: List[Dict]) -> str:
    """
    图像识别工具：只在当前买家发送信息中有图片链接时调用该工具，图片链接中一般包含gif|png|jpg|jpeg|webp|svg|psd|bmp|tif|tiff|heic等字段。否则不需要调用get_image_info工具。
    且存在买家对图片内容提出问题时调用该工具，你应该总结顾客的问题获得summarized_query，然后调用此函数，返回对于图片忠实的描述。
    Args:
        summarized_query: 基于当前历史对话记录需要对于历史对话中某个图片提出的问题
        history_messages: 所有的messages中的历史对话记录[{"role":"user","content":"***"},{"role":"assistant","content":"***"},{"tool":"assistant","content":"***"}]
    Returns:
        图片信息的格式化字符串
    """
    
    input_message = f'''
    "你是一个高级的电商客服，你要理解对话信息中发送的图片信息和文字信息之间的关系，并给出图片中和当前主要问题有关的描述。'
    请简洁准确地描述图片内容，并遵循以下要求：
    1.忠实描述图片中的主要对象、场景等信息，如果图片描述中有文字，请提取并返回文字内容。
    2.描述内容尽量突出和用户主要问题相关的信息，简介明了不超过100个字
    3.回答的格式清晰
    
    这个是历史对话记录：
    {history_messages}

    这个是用户当前的问题：
    {summarized_query}
    '''
    online_llm_api = OnlineLLMApi()
    online_llm_api.multimodal_type = "kimi-128k"
    result = online_llm_api.generate_multimodal_response(input_message).content
    return result