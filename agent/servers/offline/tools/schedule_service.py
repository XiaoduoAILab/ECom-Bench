from .utils import get_order

def schedule_service(data, platform, shop_id, order_id, user_id, user_name, phone_number, service_type, service_time):
    order = get_order(data, platform, shop_id, user_id, order_id)
    if not order:
        return data, f"没有找到{platform}店铺{shop_id}用户{user_id}订单{order_id}"
    if 'service' not in data:
        data['service'] = {}
    
    if platform not in data['service']:
        data['service'][platform] = {}
    if shop_id not in data['service'][platform]:
        data['service'][platform][shop_id] = {}
    if user_id not in data['service'][platform][shop_id]:
        data['service'][platform][shop_id][user_id] = {}
    
    record = {
        "服务类型": service_type,
        "店铺ID": shop_id,
        "用户ID": user_id,
        "订单ID": order_id,
        "平台": platform,
        "电话号码": phone_number,
        "用户姓名": user_name,
        "预约日期": service_time,
    }
    data['service'][platform][shop_id][user_id][order_id] = record
    return data, f"预约{service_type}服务成功"