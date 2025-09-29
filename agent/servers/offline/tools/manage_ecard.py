from .utils import get_user, get_product_detail

ecard_service = f"""
京东E卡是京东商城发行的电子预付卡，可用于购买京东自营商品，涵盖数码家电、服饰美妆、家居日用等多种品类。
该卡分为电子卡和实体卡两种形式，支持灵活面值选择，并可通过京东账户绑定使用，方便快捷。
京东E卡有效期为自激活之日起36个月，未使用余额可保留至有效期结束，适用于个人消费或作为礼品赠送。
需要注意的是，该卡仅限京东自营商品使用，不支持第三方卖家商品、虚拟充值及部分特殊品类。退款时，金额将退回原卡内，不可提现，确保资金安全。
京东E卡凭借其便捷性、安全性和广泛的适用范围，成为京东用户喜爱的支付方式之一。
"""

def manage_ecard(data, platform: str, user_id: str, action: str, product_id: str = None, quantity: int = None, shop_id: str = None, amount:float = 0):
    user_info = get_user(data, user_id)
    if not user_info:
        return data, f"没有找到用户{user_id}的信息"
    if action == '信息查询':
        return data, ecard_service
    elif action == '余额查询':
        return data, f"用户{user_id}的电子卡余额为{user_info['电子卡余额']}元"
    elif action == '余额使用':
        if not product_id or not quantity or not shop_id:
            return data, f"请提供商品ID、购买数量和店铺ID"
        product = get_product_detail(data, platform, shop_id, product_id)
        if not product:
            return data, f"没有找到商品{product_id}的信息"
        product_price = product.get('商品价格', 0)
        data['users_info'][user_id]['电子卡余额'] -= product_price * quantity
        return data, f"已购买{quantity}件商品{product_id}，用户{user_id}的电子卡余额为{data['users_info'][user_id]['电子卡余额']}元"
    elif action == '退款':
        data['users_info'][user_id]['电子卡余额'] += float(amount)
        return data, f"已退款{amount}元，用户{user_id}的电子卡余额为{data['users_info'][user_id]['电子卡余额']}元"