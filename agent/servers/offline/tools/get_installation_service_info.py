from .utils import get_product_detail, get_product_base
import json

def get_installation_service_info(data, platform, shop_id, product_id):
    if not product_id.isdigit():
        return data, f"商品ID{product_id}格式错误，应该为数字"
    product = get_product_detail(data, platform, shop_id, product_id)
    if not product:
        return data, f"没有找到{platform}店铺{shop_id}的商品{product_id}的信息"
    product_base = get_product_base(data, platform, shop_id, product_id)
    result = {
        **product_base,
        "安装说明": product['安装说明']
    }
    return data, json.dumps(result, ensure_ascii=False)