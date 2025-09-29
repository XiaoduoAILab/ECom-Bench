from .utils import get_order
import json

def get_user_orders_info(data, platform, shop_id, user_id):
    orders = data.get("orders", {})
    order = orders.get(platform, {}).get(shop_id, {}).get(user_id, {})
    if not order:
        return data, f"没有找到用户{user_id}的订单信息"
    result = {
        "订单ID": list(order.keys())
    }
    return data, json.dumps(result, ensure_ascii=False)
