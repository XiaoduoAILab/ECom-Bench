from typing import List,Dict
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
    return 