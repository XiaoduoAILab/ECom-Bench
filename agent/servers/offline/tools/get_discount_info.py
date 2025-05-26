from .utils import get_discount
import json 
def get_discount_info(data, platform:str, shop_id:str) -> str:
    """
    用于获取优惠信息
    当用户询问优惠政策时，可以调用此函数
    Args:
        platform: 电商平台信息
        shop_id: 店铺ID
        order_id: 订单ID
    Returns:
        优惠信息的格式化字符串
    """
    discount_info = get_discount(data = data, platform = platform, shop_id = shop_id)
    if discount_info is None:
        return f"没有找到{platform}店铺{shop_id}的优惠信息"
    return data, json.dumps(discount_info, ensure_ascii=False)