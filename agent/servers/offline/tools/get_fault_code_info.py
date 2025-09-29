from .utils import get_product_detail, get_product_base
import json

def get_fault_code_info(data, platform, shop_id, product_id, fault_code):
    if not product_id.isdigit():
        return data, f"商品ID{product_id}格式错误，应该为数字"
    product = get_product_detail(data, platform, shop_id, product_id)
    if not product:
        return data, f"没有找到{platform}店铺{shop_id}商品{product_id}的信息"
    fault_code_infos = product.get("常见故障", [])
    fault_code_info = next((x for x in fault_code_infos if x["故障代码"] == fault_code), None)
    if not fault_code_info:
        return data, f"没有找到{platform}店铺{shop_id}商品{product_id}的故障代码{fault_code}的信息"
    product_base = get_product_base(data, platform, shop_id, product_id)
    result = {
        **product_base,
        "故障信息": fault_code_info
    }
    return data, json.dumps(result, ensure_ascii=False)