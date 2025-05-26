from .utils import get_product_detail
import json
def get_repair_info(data, platform, shop_id, product_id):
    product = get_product_detail(data=data, platform=platform, shop_id=shop_id, product_id=product_id)
    if not product:
        return f"未找到商品 {product_id} 的维修信息"
    result = {
        "商品ID": product.get("商品ID", ""),
        "维修说明": product.get("维修说明", "")
    }
    return data, json.dumps(result, ensure_ascii=False)