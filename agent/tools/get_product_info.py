def get_product_info(platform: str, shop_id: str, goods_id: str) -> str:
    """
    用于获取商品信息
    当用户询问商品详情时，可以调用此函数
    Args:
        platform: 电商平台信息
        shop_id: 店铺ID
        goods_id: 商品ID
    Returns:
        商品信息的格式化字符串
    """
    return 