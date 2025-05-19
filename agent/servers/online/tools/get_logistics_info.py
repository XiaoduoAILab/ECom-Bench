import requests
import os
from .config import get_config

def get_logistics_info(platform: str, shop_id: str, order_id: str, user_id: str) -> str:
    """
    用于获取物流政策的信息
    当用户询问物流政策时，可以调用此函数
    Args:
        platform: 电商平台信息
        shop_id: 店铺ID
        order_id: 订单ID
        user_id: 用户ID
    Returns:
        物流信息的格式化字符串
    """
    config = get_config()
    url = os.path.join(config["base_url"], "get_logistics_info")
    response = requests.post(url, json={"platform": platform, "shop_id": shop_id, "order_id": order_id, "user_id": user_id})
    if response.status_code == 200:
        return response.text
    else:
        return f"请求服务器失败，状态码：{response.status_code}, 内容：{response.text}"

