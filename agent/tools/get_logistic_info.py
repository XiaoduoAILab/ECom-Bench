def get_logistic_info(platform: str, shop_id: str, order_id: str) -> str:
    """
    用于获取物流政策的信息
    当用户询问物流政策时，可以调用此函数
    Args:
        platform: 电商平台信息
        shop_id: 店铺ID
        order_id: 订单ID
    Returns:
        物流信息的格式化字符串
    """
    return 