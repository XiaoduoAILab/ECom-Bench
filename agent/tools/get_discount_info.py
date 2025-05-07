import requests
import yaml
import os
def get_discount_info(platform: str, shop_id: str, order_id: str) -> str:
    """
    用于获取优惠信息
    当用户询问优惠政策时，可以调用此函数
    Args:
        platform: 电商平台信息
        shop_id: 店铺ID
        order_id: 订单ID
    Returns:
        优惠信息的格式化字符串
    """
    base_dir = os.path.dirname(__file__)
    with open(os.path.join(base_dir, "config.yaml")):
        config = yaml.load(open(os.path.join(base_dir,"config.yaml")), Loader=yaml.FullLoader)
    url = os.path.join(config["base_url"], "get_discount_info") 
    repsponse = requests.post(url, json={"platform": platform, "shop_id": shop_id, "order_id": order_id})
    if response.status_code == 200:
        data = response.json()
        return data["discount_info"]
    else:
        return f"请求服务器失败, 状态码: {response.status_code}"