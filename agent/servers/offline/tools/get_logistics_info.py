from .utils import get_logistics
import json

def get_logistics_info(data, platform: str, shop_id: str, order_id: str, user_id: str) -> str:
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
    logistics_info = get_logistics(data = data, platform = platform, shop_id = shop_id, order_id = order_id, user_id = user_id)
    if logistics_info is None:
        return f"没有找到{platform}店铺{shop_id}用户{user_id}订单{order_id}的物流信息"
    return data, json.dumps(logistics_info, ensure_ascii=False)
    