from .utils import get_product_detail, format_product
import json


def get_product_info(data, platform, shop_id, product_id):
    if not product_id.isdigit():
        return data, f"商品ID{product_id}格式错误，应该为数字"
    product = get_product_detail(data, platform, shop_id, product_id)
    if not product:
        return data, f"没有找到{platform}店铺{shop_id}的商品{product_id}的信息"
    product = format_product(product)
    return data, json.dumps(product, ensure_ascii=False)