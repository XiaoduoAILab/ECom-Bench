from .utils import get_order, get_product_detail
import json

# 只运行修改的可换商品：1. 商品状态为已上架 2. 商品ID在可换商品列表中 3. 默认可换商品只有属性变化，例如颜色什么的，价格，数量不可以换，即只能是平替
# 可换货状态枚举：待付款，已付款，处理中
def manage_exchange(data, platform, shop_id, order_id, user_id, original_product_id, exchange_product_id):
    order = get_order(data, platform, shop_id, user_id, order_id)
    if not order:
        return data, f"没有找到{platform}店铺{shop_id}用户{user_id}订单{order_id}"
    if order.get('订单状态', '') not in ['待付款', '已付款', '处理中']:
        return data, f"订单{order_id}无法进行换货，订单状态为{order.get('订单状态', '')}"
    order_products = order.get("订单商品列表", [])
    if not any(product.get("商品ID", "") == original_product_id for product in order_products):
        return data, f"订单{order_id}购买的商品中没有找到原商品{original_product_id}"
    else:
        original_product_index = next((index for index, product in enumerate(order_products) if product.get("商品ID", "") == original_product_id), None)
    original_product = get_product_detail(data, platform, shop_id, original_product_id)
    if not original_product:
        return data, f"没有找到原商品{original_product_id}"
    exchange_list =original_product.get('可换货商品ID', [])
    if exchange_product_id not in exchange_list:
        return data, f"商品{original_product_id}不可以换货给{exchange_product_id}"
    exchange_product = get_product_detail(data, platform, shop_id, exchange_product_id)
    if not exchange_product:
        return data, f"没有找到换货商品{exchange_product_id}"
    if exchange_product.get('商品状态', '') != '已上架':
        return data, f"商品{exchange_product_id}无法进行换货，商品状态为{exchange_product.get('商品状态', '')}"
    data['orders'][platform][shop_id][user_id][order_id]['订单商品列表'][original_product_index]['商品ID'] = exchange_product_id
    return data, f"订单{order_id}商品{original_product_id}换货成功，换货后的商品ID为{exchange_product_id}"