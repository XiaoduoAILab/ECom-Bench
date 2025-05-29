from .utils import get_order
import json


# 可取消状态枚举：待付款，已付款，处理中
# 可修改地址，手机号状态枚举：待付款,已付款,处理中
def manage_order(data, platform: str, order_id: str, shop_id: str, user_id: str, action: str, address: str = None, phone_number: str = None):
    order = get_order(data, platform, shop_id, user_id, order_id)
    order_status = order.get("订单状态", "")
    if not order:
        return data, f"没有找到订单{order_id}的信息"
    if action == '查询':
        return data, json.dumps(order, ensure_ascii=False)
    elif action == '取消':
        if order_status not in ['待付款', '已付款', '处理中']:
            return data, f"订单{order_id}的状态为{order_status}，不能取消"
        data["orders"][platform][shop_id][user_id][order_id]["订单状态"] = "已取消"
        return data, f"订单{order_id}已取消"
    elif action == '修改':
        if order_status not in ['待付款', '已付款', '处理中']:
            return data, f"订单{order_id}的状态为{order_status}，不能修改"
        if not address and not phone_number:
            return data, f"新地址和新手机号都为空，无法修改"
        if address: # 默认只修改详细地址
            data["orders"][platform][shop_id][user_id][order_id]["收货地址"]["详细地址"] = address
        if phone_number:
            data["orders"][platform][shop_id][user_id][order_id]["收货地址"]["电话号码"] = phone_number
        return data, f"订单{order_id}的地址和手机号已修改"
    else:
        return data, f"不支持的操作{action}"
            