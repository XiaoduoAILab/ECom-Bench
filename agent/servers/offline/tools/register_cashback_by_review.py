from collections import defaultdict

def register_cashback_by_review(data, platform, shop_id, user_id, order_id, action):
    if not data.get("register_cashback", None):
        data["register_cashback"] = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(bool))))
    if action == "查询":
        record = data.get("register_cashback", {}).get(platform, {}).get(shop_id, {}).get(user_id, {}).get(order_id, {})
        if not record:
            return data, f"没有找到{platform}店铺{shop_id}用户{user_id}订单{order_id}的晒单返现记录（未晒单）"
        return data, f"确认查询到{platform}店铺{shop_id}用户{user_id}订单{order_id}的晒单返现记录（已晒单）"
    elif action == '返现':
        try:
            data["register_cashback"][platform][shop_id][user_id][order_id] = True
            return data, f"{platform}店铺{shop_id}用户{user_id}订单{order_id}的晒单返现已经进入返现流程（返现成功）"
        except:
            data["register_cashback"] = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(bool))))
            data["register_cashback"][platform][shop_id][user_id][order_id] = True
            return data, f"{platform}店铺{shop_id}用户{user_id}订单{order_id}的晒单返现已经进入返现流程（返现成功）"
        