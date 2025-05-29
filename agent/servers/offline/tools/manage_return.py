from .utils import get_order
import json
# 可退货退款状态枚举：已签收
def manage_return(data, platform: str, shop_id: str, order_id: str, user_id: str, action:str) -> str:
    """
    处理退货申请
    """
    order = get_order(data = data, platform = platform, shop_id = shop_id, order_id = order_id, user_id = user_id)
    if not order:
        return data, f"未能找到{platform}店铺{shop_id}用户{user_id}订单{order_id}的订单信息"
    order_status = order.get("订单状态", "")
    if action == '查询':
        if order_status == '已签收':
            return data, "可以申请退货"
        else:
            return data, f"订单状态为{order_status}，不可以申请退货"
    elif action == '处理':
        if order_status == '已签收':
            data["orders"][platform][shop_id][user_id][order_id]["订单状态"] = "已退货"
            return data, "退货申请已进行处理"
        else:
            return data, f"订单状态为{order_status}，不可以申请退货"
    else:
        return data, "无效的操作"