from pydantic import config
import requests
import os
from .config import get_config

def get_goods_property(platform: str, shop_id: str, goods_id: str) -> str:
    """
    用于获取商品信息
    当用户询问商品详情时，可以调用此函数
    Args:
        platform: 电商平台信息
        shop_id: 店铺ID
        goods_id: 商品ID
    Returns:
        商品信息的格式化字符串
    """
    config = get_config()
    url = os.path.join(config["base_url"], "get_goods_property")
    response = requests.post(url, json={"platform": platform, "shop_id": shop_id, "goods_id": goods_id})
    if response.status_code == 200:
        return response.text
    else:
        return f"请求服务器失败，状态码：{response.status_code}， 内容：{response.text}"