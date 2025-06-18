from typing import List, Dict, Annotated, Literal
from pydantic import Field, BaseModel
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
from tools import get_user_orders_info
from tools import get_auxiliary_materials_info
from tools import get_user_info

mcp = FastMCP("service")
data = None
logger = None
cache_dir = None


@mcp.tool()
def get_user_info_tool(
    user_id: Annotated[
        str,
        Field(..., description="用户ID")
    ]
) -> str:
    """
    用于获取默认的用户信息。当需要查询用户保存的相关用户信息时，可以调用此工具。
    """
    global data
    data, result = get_user_info(data = data, user_id = user_id)
    set_data(data)
    return result
    

@mcp.tool()
def get_user_orders_info_tool(
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
    用于根据用户ID获取用户所有的订单ID。
    """
    global data
    data, result = get_user_orders_info(data = data, platform = platform, shop_id = shop_id, user_id = user_id)
    set_data(data)
    return result

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
    global data
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
    global data
    data, result = get_discount_info(data = data, platform = platform, shop_id = shop_id)
    set_data(data)
    return result



@mcp.tool()
def get_image_info_tool(
    summarized_query: Annotated[
        str,
        Field(..., description="根据上下文总结顾客对图片的需求（用于任务提示）")
    ], 
    needed_query: Annotated[
        str,
        Field(..., description="总结希望从图片中提取到的信息内容")
    ],
    history_messages: Annotated[
        str,
        Field(..., description="对话上下文，必须包含图片完整链接。")
    ]
) -> str:
    """
    图像识别工具：仅在以下情况调用：
    1. 当前或历史消息中包含图片链接（如含 `gif|png|jpg|jpeg|webp|svg|psd|bmp|tif|tiff|heic` 等扩展名），调用时必须包含完整图片链接
    2. 你需要从图片中获取图片内容信息来解决问题
    """
    global data
    data, result = get_image_info(data, summarized_query, needed_query, history_messages)
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
) -> str:
    """
    用于处理退货服务的信息。当用户需要申请退货时，可以调用此工具。
    """
    global data
    data, result = manage_return(data = data, platform = platform, shop_id = shop_id, order_id = order_id, user_id = user_id)
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
    action: Annotated[
        Literal["查询", "换货"],
        Field(..., description="操作类型，'查询'为查询换货信息，'换货'为处理换货申请")
    ],
    exchange_product_id: Annotated[
        str,
        Field(None, description="换货商品ID，仅在action为'换货'时必填")
    ] = None
) -> str:
    """
    用于处理换货服务。当用户需要提交换货申请时，可以调用此工具。
    """
    global data
    data, result = manage_exchange(data = data, platform = platform, shop_id = shop_id, order_id = order_id, user_id = user_id, original_product_id = original_product_id, exchange_product_id = exchange_product_id, action = action)
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
    用于处理发货、运输加急服务的工具。当用户需要加急发货、运输服务时,可以调用此工具。
    """
    global data
    data, result = manage_urgent(data = data, platform = platform, shop_id = shop_id, order_id = order_id, user_id = user_id)
    set_data(data)
    return result

@mcp.tool()

def get_auxiliary_materials_info_tool(
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
    用于获取商品的辅材信息。当用户询问商品辅材信息时，可以调用此工具。
    """
    global data
    data, result = get_auxiliary_materials_info(data = data, platform = platform, shop_id = shop_id, product_id = product_id)
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
    data, result = get_gift_info(data= data, platform = platform, shop_id = shop_id, product_id = product_id)
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
        Literal["信息查询", "余额使用", "余额查询", "退款"],
        Field(..., description="操作类型，可选值：信息查询（查询京东E卡相关信息）、余额使用、余额查询、退款")
    ],
    shop_id: Annotated[
        str,
        Field(None, description="店铺ID（仅在action为余额使用时必填）")
    ] = None,
    product_id: Annotated[
        str,
        Field(None, description="商品ID（仅在action为余额使用时必填）")
    ] = None,
    quantity: Annotated[
        int,
        Field(None, description="商品购买数量（仅在action为余额使用时必填）")
    ] = None,
    amount: Annotated[
        float,
        Field(0, description="退款金额（仅在action为退款时必填）")
    ] = None
) -> str:
    """
    用于管理京东E卡信息（查询服务、使用、余额查询、退款）。当用户提出有关京东E卡相关问题时，可以调用此工具。
    """
    global data
    data, result = manage_ecard(data = data, platform = platform, user_id = user_id, action = action, product_id = product_id, quantity = quantity, shop_id = shop_id, amount = amount)
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
    用于获取商品安装服务信息或问题。当用户询问安装服务，安装流程时，可以调用此工具。
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
    用于获取商品详情。当用户询问商品信息时，可以调用此工具。
    """
    global data
    data, result = get_product_info(data = data, platform = platform, shop_id = shop_id, product_id = product_id)
    set_data(data)
    return result

class ProductInfo(BaseModel):
    product_id: Annotated[
        str,
        Field(..., description="商品ID")
    ]
    quantity: Annotated[
        int,
        Field(..., description="商品数量")
    ]
    

@mcp.tool()
def manage_order_tool(
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
    action: Annotated[
        Literal["查询", "取消", "修改", "增加"],
        Field(..., description="操作类型，可选值：查询、取消、修改（地址/手机号）、增加（下订单）")
    ],
    payment: Annotated[
        Literal["银行卡", "京东E卡", "微信", "支付宝"],
        Field('支付宝', description="支付方式（仅在action为增加时必填）")
    ] = None,
    order_id: Annotated[
        str,
        Field(None, description="订单ID（仅在action为查询、取消、修改时必填）")
    ] = None,
    address: Annotated[
        str,
        Field(None, description="新收货地址（仅在action为修改时选填）")
    ] = None,
    phone_number: Annotated[
        str,
        Field(None, description="新手机号（仅在action为修改时选填）")
    ] = None,
    product_info_list: Annotated[
        List[ProductInfo],
        Field(None, description="商品信息（仅在action为增加时必填）")
    ] = None
) -> str:
    """
    用于管理订单信息，包括查询订单、取消订单（需要向用户再次确认）、修改订单（地址、手机号）、下订单操作。
    订单的信息包括用户购买的商品，收货地址等具体信息
    """
    global data
    data, result = manage_order(data = data, platform = platform, order_id = order_id, shop_id = shop_id, user_id = user_id, action = action, address = address, phone_number = phone_number, product_info_list = product_info_list, payment = payment)
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
    处理电商平台晒单返现的查询与返现流程。
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
