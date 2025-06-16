from .utils import get_product_detail, get_product_base
import json
def get_repair_info(data, platform, shop_id, product_id):
    product = get_product_detail(data=data, platform=platform, shop_id=shop_id, product_id=product_id)
    if not product:
        return f"未找到商品 {product_id} 的维修信息"
    product_base = get_product_base(data=data, platform=platform, shop_id=shop_id, product_id=product_id)
    result = {
        **product_base,
        "维修说明": product.get("维修说明", "")
    }
    
    return data, json.dumps(result, ensure_ascii=False)