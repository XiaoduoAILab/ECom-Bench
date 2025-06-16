from .utils import get_product_detail, get_product_base
import json

def get_auxiliary_materials_info(data, platform, shop_id, product_id):
    if not product_id.isdigit():
        return data, f"商品ID{product_id}格式错误，应该为数字"
    product = get_product_detail(data, platform, shop_id, product_id)
    if not product:
        return data, f"没有找到{platform}店铺{shop_id}的商品{product_id}的信息"
    auxiliary_materials = product.get("辅材材料", [])
    if not auxiliary_materials:
        return data, f"商品{product_id}没有辅材材料"
    product_base = get_product_base(data, platform, shop_id, product_id)
    result = {
        **product_base,
        "辅材材料": auxiliary_materials
    }
    return data, json.dumps(result, ensure_ascii=False)
