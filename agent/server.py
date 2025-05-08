from typing import List, Dict
from mcp.server.fastmcp import FastMCP
from tools import get_discount_info
from tools import get_image_info
from tools import get_logistic_info
from tools import get_order_info
from tools import get_goods_property
mcp = FastMCP("service")


@mcp.tool()
def get_logistic_info_tool(platform: str, shop_id: str, order_id: str) -> str:
    """
    用于获取物流政策的信息
    当用户询问物流政策时，可以调用此工具
    Args:
        platform: 电商平台信息
        shop_id: 店铺ID
        order_id: 订单ID
    Returns:
        物流政策的格式化字符串
    """
    return get_logistic_info(platform, shop_id, order_id)

@mcp.tool()
def gget_goods_property_tool(platform: str, shop_id: str, goods_id: str) -> str:
    """
    用于获取商品信息
    当用户询问商品详情时，可以调用此工具
    Args:
        platform: 电商平台信息
        shop_id: 店铺ID
        goods_id: 商品ID
    Returns:
        商品信息的格式化字符串
    """
    return get_goods_property(platform, shop_id, goods_id)

@mcp.tool()
def get_discount_info_tool(platform: str, shop_id: str, order_id: str) -> str:
    """
    用于获取优惠信息
    当用户询问优惠政策时，可以调用此工具
    Args:
        platform: 电商平台信息
        shop_id: 店铺ID
        order_id: 订单ID
    Returns:
        优惠信息的格式化字符串
    """
    return get_discount_info(platform, shop_id, order_id)

@mcp.tool()
def get_order_info_tool(platform: str, order_id: str):
    """
    用于获取订单的信息
    当用户询问订单相关问题时，可以调用此工具
    Args:
        platform: 电商平台信息
        order_id: 订单ID
    Returns:
        订单信息的格式化字符串
    """
    return get_order_info(platform, order_id)

@mcp.tool()
def get_image_info_tool(
    summarized_query: str, 
    history_messages: List[Dict[str, str]]
) -> str:
    """
    图像识别工具：仅在以下情况调用：
    1. 当前或历史消息中包含图片链接（如含 `gif|png|jpg|jpeg|webp|svg|psd|bmp|tif|tiff|heic` 等扩展名）。
    2. 买家明确对图片内容提出问题（如询问包装、颜色、尺寸、细节等）。

    否则不应调用此工具，避免无效请求。

    Args:
        summarized_query (str): 从对话中提炼的关于图片的核心问题（如“包装是什么样子的？”）。
        history_messages (List[Dict]): 完整对话历史，格式为：
            [
                {"role": "user", "content": "图片链接或文字描述"},
                {"role": "assistant", "content": "回复内容"},
                ...
            ]
            注：必须包含图片链接，否则工具调用无效。

    Returns:
        str: 对图片的忠实描述，格式为：
            - 若识别成功：返回结构化信息（如“包装为蓝色长方体，尺寸10cm×20cm”）。
            - 若无图片链接：返回“未检测到有效图片链接”。
            - 若识别失败：返回“无法识别图片内容”。
    """
    return get_image_info(summarized_query, history_messages)

if __name__ == "__main__":
    mcp.run(transport="stdio")