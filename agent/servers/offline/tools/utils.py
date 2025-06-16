

def get_logistics(data, platform: str, shop_id: str, order_id: str, user_id: str):
    logistics_data = data.get("logistics", {})
    logistics = logistics_data.get(platform, {}).get(shop_id, {}).get(user_id, {}).get(order_id, {})
    if not logistics:
        return None
    return logistics

def get_product_base(data, platform: str, shop_id: str, product_id: str):
    product_data = data.get("products", {})
    product = product_data.get(platform, {}).get(shop_id, {}).get(product_id, {})
    if not product:
        return None
    return {
        "商品ID": product["商品ID"],
        "商品名称": product["商品名称"]
    }

def get_product_detail(data, platform: str, shop_id: str, product_id: str):
    product_data = data.get("products", {})
    product = product_data.get(platform, {}).get(shop_id, {}).get(product_id, {})
    if not product:
        return None
    return product


def get_order(data, platform: str, shop_id: str, user_id: str, order_id: str):
    order_data = data.get("orders", {})
    order = order_data.get(platform, {}).get(shop_id, {}).get(user_id, {}).get(order_id, {})
    if not order:
        return None
    return order

def get_discount(data, platform: str, shop_id: str):
    discount_data = data.get("discount", {})
    discount = discount_data.get(platform, {}).get(shop_id, {})
    if not discount:
        return None
    return discount

def get_user(data, user_id: str):
    user_data = data.get("users_info", {})
    user = user_data.get(user_id, {})
    if not user:
        return None
    return user

def format_product(product):
    product_formatted = {
        "商品ID": product["商品ID"],
        "商品名称": product["商品名称"],
        "商品状态": product["商品状态"],
        "商品价格": product["商品价格"],
        "商品描述": product["商品描述"]
    }
    return product_formatted
