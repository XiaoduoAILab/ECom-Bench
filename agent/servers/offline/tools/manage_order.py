from .utils import get_order, get_user, get_product_detail
import json

# 可取消状态枚举：待付款，已付款，处理中
# 可修改地址，手机号状态枚举：待付款,已付款,处理中

def manage_order(data, platform: str, shop_id: str, user_id: str, action: str, order_id:str = None, address: str = None, phone_number: str = None, product_info_list = None, payment:str ='支付宝'):
    if action == '增加':
        order_id = '1234567890'
        if len(product_info_list) == 0:
            return data, f"商品列表为空，无法进行下单"
        user_info = get_user(data, user_id)
        if not user_info:
            return data, f"没有找到用户{user_id}的信息"
        recipient = {
            '收件人姓名': user_info['用户姓名'],
            '电话号码': user_info['电话号码'],
            '国家': user_info['地址信息']['国家'],
            '省份': user_info['地址信息']['省份'],
            '城市': user_info['地址信息']['城市'],
            '区县': user_info['地址信息']['区县'],
            '详细地址': user_info['地址信息']['详细地址']
        }
        total_amount = 0
        order_product_list = []
        for product_info in product_info_list:
            product_id = product_info.product_id
            quantity = product_info.quantity
            product = get_product_detail(data, platform, shop_id, product_id)
            if not product:
                continue
            order_product_list.append({
                '商品ID': product_id,
                '商品价格': product['商品价格'],
                '数量': quantity,
            })
            total_amount += product['商品价格'] * quantity
        order = {
            '用户ID': user_id,
            '订单ID': order_id,
            '订单状态': '已付款',
            '订单总金额': total_amount,
            '是否加急': False,
            '订单商品列表': order_product_list,
            '收货地址': recipient,
            '支付方式': payment,
        }
        if platform not in data["orders"]:
            data["orders"][platform] = {}
        if shop_id not in data["orders"][platform]:
            data["orders"][platform][shop_id] = {}
        if user_id not in data["orders"][platform][shop_id]:
            data["orders"][platform][shop_id][user_id] = {}
        data["orders"][platform][shop_id][user_id][order_id] = order
        return data, f"订单{order_id}已增加,具体订单内容：{json.dumps(order, ensure_ascii=False)}"
    order = get_order(data, platform, shop_id, user_id, order_id)
    if not order:
        return data, f"没有找到订单{order_id}的信息"
    if action == '查询':
        return data, json.dumps(order, ensure_ascii=False)
    elif action == '取消':
        data["orders"][platform][shop_id][user_id][order_id]["订单状态"] = "已取消"
        return data, f"订单{order_id}已取消，取消的订单是{json.dumps(order, ensure_ascii=False)}"
    elif action == '修改':
        if not address and not phone_number:
            return data, f"新地址和新手机号都为空，无法修改"
        if address: # 默认只修改详细地址
            data["orders"][platform][shop_id][user_id][order_id]["收货地址"]["详细地址"] = address
        if phone_number:
            data["orders"][platform][shop_id][user_id][order_id]["收货地址"]["电话号码"] = phone_number
        return data, f"订单{order_id}的地址和手机号已修改，修改后的订单是{json.dumps(order, ensure_ascii=False)}"
    else:
        return data, f"不支持的操作{action}"
            