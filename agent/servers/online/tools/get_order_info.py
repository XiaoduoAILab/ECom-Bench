import requests
import os
from .config import get_config
def get_order_info(platform: str, order_id: str):
    """
    用于获取订单的信息
    当用户询问订单相关问题时，可以调用此工具
    Args:
        platform: 电商平台信息
        order_id: 订单ID
    Returns:
        订单信息的格式化字符串
    """
    config = get_config()
    url = os.path.join(config["base_url"], "get_order_info")
    response = requests.post(url, json={"platform": platform, "order_id": order_id})
    if response.status_code == 200:
        return response.text
    else:
        return f"请求服务器失败, 状态码：{response.status_code}，内容：{response.text}"