from .utils import get_order
import json
# 可退货退款状态枚举：已签收
def manage_return(data, platform: str, shop_id: str, order_id: str, user_id: str) -> str:
    """
    处理退货申请
    """
    order = get_order(data, platform, shop_id, user_id, order_id)
    if not order:
        return data, f"没有找到订单{order_id}的信息"
    data["orders"][platform][shop_id][user_id][order_id]["订单状态"] = "已退货"
    return data, f"退货申请已进行处理, 退货的订单是{json.dumps(order, ensure_ascii=False)}"