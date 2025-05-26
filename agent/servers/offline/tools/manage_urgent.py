from .utils import get_order

def manage_urgent(data, platform, shop_id, order_id, user_id):
    order = get_order(data, platform, shop_id, user_id, order_id)
    if not order:
        return data, f"没有找到{platform}店铺{shop_id}用户{user_id}订单{order_id}"
    data["orders"][platform][shop_id][user_id][order_id]["是否加急"] = True
    return data, f"已将{platform}店铺{shop_id}用户{user_id}订单{order_id}设置为加急"
        