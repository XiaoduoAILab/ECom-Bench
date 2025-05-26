from typing import List, Dict, Annotated, Literal
from pydantic import Field
import os
import json
from mcp.server.fastmcp import FastMCP
from tools import compare_products_info
from tools import get_discount_info
from tools import get_fault_code_info
from tools import get_gift_info
from tools import get_image_info
from tools import get_installation_service_info
from tools import get_logistics_info
from tools import get_product_info
from tools import get_repair_info
from tools import manage_ecard
from tools import manage_exchange
from tools import manage_invoice
from tools import manage_order
from tools import manage_return
from tools import manage_urgent
from tools import register_cashback_by_review
from tools import schedule_service
from tools import transfer_to_specialist
from tools import set_up_logger


mcp = FastMCP("service")
data = None
logger = None
cache_dir = None

@mcp.tool()
def get_logistics_info_tool(
    platform: Annotated[
        str,
        Field(..., description="电商平台")
    ],
    shop_id: Annotated[
        str,
        Field(..., description="店铺ID")
    ],
    order_id: Annotated[
        str,
        Field(..., description="订单ID")
    ],
    user_id: Annotated[
        str,
        Field(..., description="用户ID")
    ]
) -> str:
    """
    用于获取物流政策的信息
    当用户询问物流相关的问题时，可以调用此工具
    """
    data, result = get_logistics_info(data = data, platform = platform, shop_id = shop_id, order_id = order_id, user_id = user_id)
    set_data(data)
    return result


@mcp.tool()
def get_discount_info_tool(
    platform: Annotated[
        str,
        Field(..., description="电商平台")
    ],
    shop_id: Annotated[
        str,
        Field(..., description="店铺ID")
    ]
) -> str:
    """
    用于获取优惠信息
    当用户询问优惠政策时，可以调用此工具
    """
    data, result = get_discount_info(data = data, platform = platform, shop_id = shop_id)
    set_data(data)
    return result



@mcp.tool()
def get_image_info_tool(
    summarized_query: Annotated[
        str,
        Field(..., description="从对话中提炼的关于图片的核心问题（如包装是什么样子的？）")
    ], 
    history_messages: Annotated[
        List[Dict[str, str]],
        Field(..., description="完整对话历史，格式为：[{\"role\": \"user\", \"content\": \"图片链接或文字描述\"}, {\"role\": \"assistant\", \"content\": \"回复内容\"}, ...]")
    ]
) -> str:
    """
    图像识别工具：仅在以下情况调用：
    1. 当前或历史消息中包含图片链接（如含 `gif|png|jpg|jpeg|webp|svg|psd|bmp|tif|tiff|heic` 等扩展名）。
    """
    global data
    data, result = get_image_info(data, summarized_query, history_messages)
    set_data(data)
    return result

@mcp.tool()
def get_repair_info_tool(
    platform: Annotated[
        str,
        Field(..., description="电商平台")
    ],
    shop_id: Annotated[
        str,
        Field(..., description="店铺ID")
    ],
    product_id: Annotated[
        str,
        Field(..., description="商品ID")
    ]
) -> str:
    """
    用于获取维修服务的信息。当用户询问维修服务时,可以调用此工具。
    """
    global data
    data, result = get_repair_info(data = data, platform = platform, shop_id = shop_id, product_id = product_id)
    set_data(data)
    return result

@mcp.tool()
def manage_return_tool(
    platform: Annotated[
        str,
        Field(..., description="电商平台")
    ],
    shop_id: Annotated[
        str,
        Field(..., description="店铺ID")
    ],
    order_id: Annotated[
        str,
        Field(..., description="订单ID")
    ],
    user_id: Annotated[
        str,
        Field(..., description="用户ID")
    ],
    action: Annotated[
        Literal["query", "handle"],
        Field(..., description="操作类型，'query'为查询退货信息，'handle'为处理退货申请")
    ]
) -> str:
    """
    用于获取或处理退货服务的信息。当用户需要查询退货信息或申请退货时，可以调用此工具。
    """
    global data
    data, result = manage_return(data = data, platform = platform, shop_id = shop_id, order_id = order_id, user_id = user_id, action = action)
    set_data(data)
    return result

@mcp.tool()
def manage_exchange_tool(
    platform: Annotated[
        str,
        Field(..., description="电商平台")
    ],
    shop_id: Annotated[
        str,
        Field(..., description="店铺ID")
    ],
    order_id: Annotated[
        str,
        Field(..., description="订单ID")
    ],
    user_id: Annotated[
        str,
        Field(..., description="用户ID")
    ],
    original_product_id: Annotated[
        str,
        Field(..., description="原商品ID")
    ],
    exchange_product_id: Annotated[
        str,
        Field(..., description="换货商品ID")
    ]
) -> str:
    """
    用于处理换货服务。当用户需要提交换货申请时，可以调用此工具。
    """
    global data
    data, result = manage_exchange(data = data, platform = platform, shop_id = shop_id, order_id = order_id, user_id = user_id, original_product_id = original_product_id, exchange_product_id = exchange_product_id)
    set_data(data)
    return result

@mcp.tool()
def manage_urgent_tool(
    platform: Annotated[
        str,
        Field(..., description="电商平台")
    ],
    shop_id: Annotated[
        str,
        Field(..., description="店铺ID")
    ],
    order_id: Annotated[
        str,
        Field(..., description="订单ID")
    ],
    user_id: Annotated[
        str,
        Field(..., description="用户ID")
    ]
) -> bool:
    """
    用于处理加急服务的工具。当用户需要加急服务时,可以调用此工具。
    """
    global data
    data, result = manage_urgent(data = data, platform = platform, shop_id = shop_id, order_id = order_id, user_id = user_id)
    set_data(data)
    return result

@mcp.tool()
def get_gift_info_tool(
    platform: Annotated[
        str,
        Field(..., description="电商平台")
    ],
    shop_id: Annotated[
        str,
        Field(..., description="店铺ID")
    ],
    product_id: Annotated[
        str,
        Field(..., description="商品ID")
    ]
) -> str:
    """
    用于获取赠品信息。当用户询问赠品相关问题时，可以调用此工具。
    """
    global data
    data, result = get_gift_info(data)
    set_data(data)
    return result

@mcp.tool()
def manage_ecard_tool(
    platform: Annotated[
        str,
        Field(..., description="电商平台")
    ],
    user_id: Annotated[
        str,
        Field(..., description="用户ID")
    ],
    action: Annotated[
        Literal["query", "usage", "balance"],
        Field(..., description="操作类型，可选值：query（查询ecard相关信息）、usage（使用）、balance（余额查询）")
    ],
    shop_id: Annotated[
        str,
        Field(None, description="店铺ID（仅在action为usage时必填）")
    ] = None,
    product_id: Annotated[
        str,
        Field(None, description="商品ID（仅在action为usage时必填）")
    ] = None,
    quantity: Annotated[
        int,
        Field(None, description="商品购买数量（仅在action为usage时必填）")
    ] = None
) -> str:
    """
    用于管理京东E卡信息（查询使用方法、使用、余额）。当用户提出有关京东E卡相关问题时，可以调用此工具。
    """
    global data
    data, result = manage_ecard(data = data, platform = platform, user_id = user_id, action = action, product_id = product_id, quantity = quantity, shop_id = shop_id)
    set_data(data)
    return result

@mcp.tool()
def get_installation_service_info_tool(
    platform: Annotated[
        str,
        Field(..., description="电商平台")
    ],
    shop_id: Annotated[
        str,
        Field(..., description="店铺ID")
    ],
    product_id: Annotated[
        str,
        Field(..., description="商品ID")
    ]
) -> str:
    """
    用于获取安装服务信息或问题。当用户询问安装服务时，可以调用此工具。
    """
    global data
    data, result = get_installation_service_info(data = data, platform = platform, shop_id = shop_id, product_id = product_id)
    set_data(data)
    return result

@mcp.tool()
def get_product_info_tool(
    platform: Annotated[
        str,
        Field(..., description="电商平台")
    ],
    shop_id: Annotated[
        str,
        Field(..., description="店铺ID")
    ],
    product_id: Annotated[
        str,
        Field(..., description="商品ID")
    ]
) -> str:
    """
    用于获取商品详情（属性、质保、噪音、辅材,）。当用户询问商品信息时，可以调用此工具。
    """
    global data
    data, result = get_product_info(data = data, platform = platform, shop_id = shop_id, product_id = product_id)
    set_data(data)
    return result

@mcp.tool()
def manage_order_tool(
    platform: Annotated[
        str,
        Field(..., description="电商平台")
    ],
    order_id: Annotated[
        str,
        Field(..., description="订单ID")
    ],
    shop_id: Annotated[
        str,
        Field(..., description="店铺ID")
    ],
    user_id: Annotated[
        str,
        Field(..., description="用户ID")
    ],
    action: Annotated[
        Literal["query", "cancel", "modify"],
        Field(..., description="操作类型，可选值：query（查询）、cancel（取消）、modify（修改地址/手机号）")
    ],
    address: Annotated[
        str,
        Field(None, description="新收货地址（仅在action为modify时选填）")
    ] = None,
    phone_number: Annotated[
        str,
        Field(None, description="新手机号（仅在action为modify时选填）")
    ] = None
) -> str:
    """
    用于管理订单信息，包括查询订单、取消订单（需要向用户再次确认）、修改订单（地址、手机号）操作。
    """
    global data
    data, result = manage_order(data = data, platform = platform, order_id = order_id, shop_id = shop_id, user_id = user_id, action = action, address = address, phone_number = phone_number)
    set_data(data)
    return result

@mcp.tool()
def schedule_service_tool(
    platform: Annotated[
        str,
        Field(..., description="电商平台")
    ],
    shop_id: Annotated[
        str,
        Field(..., description="店铺ID")
    ],
    order_id: Annotated[
        str,
        Field(..., description="订单ID")
    ],
    user_id: Annotated[
        str,
        Field(..., description="用户ID")
    ],
    user_name: Annotated[
        str,
        Field(..., description="用户姓名")
    ],
    phone_number: Annotated[
        str,
        Field(..., description="用户电话号码")
    ],
    service_type: Annotated[
        Literal["维修", "检查", "安装"],
        Field(..., description="用户需要的服务类型")
    ],
    service_time: Annotated[
        Literal["周一", "周二", "周三", "周四", "周五", "周六", "周日"],
        Field(..., description="用户预约服务的时间")
    ],
) -> str:
    """
    用于用户想要预约维修、上门检查、安装服务。
    """
    global data
    data, result = schedule_service(data = data, platform = platform, shop_id = shop_id, order_id = order_id, user_id = user_id, user_name = user_name, phone_number = phone_number, service_type = service_type, service_time = service_time)
    set_data(data)
    return result



# @mcp.tool()
# def get_products_recommendation_tool(
#     platform: Annotated[
#         str,
#         Field(..., description="电商平台")
#     ],
#     shop_id: Annotated[
#         str,
#         Field(..., description="店铺ID")
#     ],
#     properties: Annotated[
#         dict,
#         Field(..., description="商品的属性信息")
#     ]
# ) -> str:
#     """
#     用于获取产品推荐信息。当用户询问产品推荐时,可以调用此工具。
#     """
#     data, result = get_products_recommendation(data = data, platform = platform, shop_id = shop_id, properties = properties)
#     set_data(data)
#     return result

@mcp.tool()
def get_fault_code_info_tool(
    platform: Annotated[
        str,
        Field(..., description="电商平台")
    ],
    shop_id: Annotated[
        str,
        Field(..., description="店铺ID")
    ],
    product_id: Annotated[
        str,
        Field(..., description="商品ID")
    ],
    fault_code: Annotated[
        str,
        Field(..., description="商品故障码")
    ]
) -> str:
    """
    用于获取商品故障码对应的故障信息。当用户反馈商品故障码时,可以调用此工具。
    """
    global data
    data, result = get_fault_code_info(data = data, platform = platform, shop_id = shop_id, product_id = product_id, fault_code = fault_code)
    set_data(data)
    return result

@mcp.tool()
def register_cashback_by_review_tool(
    platform: Annotated[
        str,
        Field(..., description="电商平台")
    ],
    shop_id: Annotated[
        str,
        Field(..., description="店铺ID")
    ],
    user_id: Annotated[
        str,
        Field(..., description="用户ID")
    ],
    order_id: Annotated[
        str,
        Field(..., description="订单ID")
    ],
    action: Annotated[
        Literal["查询", "返现"],
        Field(..., description="操作类型：'查询'-检查晒单状态，'返现'-在确认已经晒单基础上进行返现")
    ]
) -> str:
    """
    处理电商平台晒单返现的查询与登记流程。
    
    操作流程：
    1. 当action为'查询'时：
        - 检查系统是否已有该订单的晒单记录
        - 返回当前晒单状态（已晒单/未晒单）
    
    2. 当action为'返现'时：
        - 若系统无晒单记录，会要求用户提供晒单凭证（如截图链接）
        - 你需要通过工具验证凭证有效后，登记晒单信息并触发返现流程
    """
    global data
    data, result = register_cashback_by_review(data = data, platform = platform, shop_id = shop_id, user_id = user_id, order_id = order_id, action = action)
    set_data(data)
    return result

@mcp.tool()
def compare_products_info_tool(
    shop_id: Annotated[
        str,
        Field(..., description="店铺ID")
    ],
    platform: Annotated[
        str,
        Field(..., description="电商平台")
    ],
    product_ids: Annotated[
        List[str],
        Field(..., description="待对比的商品ID列表")
    ]
) -> str:
    """
    用于对比同一店铺下多个商品的信息。当用户需要对比商品参数、配置、价格等信息时，可以调用此工具。
    """
    global data
    data, result = compare_products_info(data = data, shop_id = shop_id, platform = platform, product_ids = product_ids)
    set_data(data)
    return result

@mcp.tool()
def manage_invoice_tool(
    title:Annotated[
        str,
        Field(..., description="发票抬头，如公司名称或个人姓名")
    ],
    order_id: Annotated[
        str,
        Field(..., description="订单ID")
    ],
    phone_number: Annotated[
        str,
        Field(..., description="联系电话")
    ],
    invoice_type: Annotated[
        Literal["个人发票", "企业发票", "增值税专用发票"],
        Field(..., description="发票类型，可选值：个人发票、企业发票、增值税专用发票，需要用户提供")
    ]
    ) -> str:
    """
    用于申请开具发票。当用户需要开具发票时，可以调用此工具。
    """
    global data
    data, result = manage_invoice(data = data, title = title, order_id = order_id, phone_number = phone_number, invoice_type = invoice_type)
    set_data(data)
    return result

@mcp.tool()
def transfer_to_specialist_tool(
    platform: Annotated[
        str,
        Field(..., description="电商平台")
    ],
    shop_id: Annotated[
        str,
        Field(..., description="店铺ID")
    ],
    user_id: Annotated[
        str,
        Field(..., description="用户ID")
    ]
) -> str:
    """
    用于转接至相应专线客服。当客服需要转接买家至专线客服时,可以调用此工具。
    """
    global data
    data, result = transfer_to_specialist(data, platform, shop_id, user_id)
    set_data(data)
    return result




    
def set_data(data):
    for file_name, file_data in data.items():
        file_path = os.path.join(cache_dir, file_name + '.json')
        with open(file_path, 'w',encoding='utf-8') as f:
            json.dump(file_data, f, ensure_ascii=False, indent=2)
    

def get_data(cache_dir):
    # 从指定目录下读取所有json文件
    data = {}
    files = os.listdir(cache_dir)
    json_files = [f for f in files if f.endswith('.json')]
    if len(json_files) == 0:
        return {}
    else:
        # 读取最新的json文件
        for json_file in json_files:
            file_path = os.path.join(cache_dir, json_file)
            file_name = os.path.splitext(json_file)[0]
            with open(file_path, 'r',encoding='utf-8') as f:
                data[file_name] = json.load(f)
    return data

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="MultiServerMCPClient")
    parser.add_argument("--cache_dir", type=str, default="cache", help="Cache directory")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    cache_dir = args.cache_dir
    logger = set_up_logger()
    data = get_data(args.cache_dir)
    mcp.run(transport="stdio")