from .utils import get_product_detail,format_product
import json

def compare_products_info(data, shop_id, platform, product_ids):
    products = []
    for product_id in product_ids:
        product = get_product_detail(data, platform, shop_id, product_id)
        if not product:
            return data, f"没有找到{platform}店铺{shop_id}商品{product_id}的信息"
        products.append(format_product(product))
    return data, json.dumps(products, ensure_ascii=False)