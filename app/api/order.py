import requests
from fastapi import APIRouter
from pydantic import BaseModel
from utils.common import center
from utils.cache import get_md5, read_cache, write_cache
from utils.config import get_config

# 创建路由
router = APIRouter()

# 订单状态映射字典
ORDER_STATUS_DICT = {
    "unknown": "未知",
    "created": "订单创建",
    "ungroup": "待成团",  # 目前仅pdd
    "deposited": "收到对账消息，且实付等于定金应付",
    "unpaid_deposit": "收到对账消息，且实付小于定金应付",
    "excessive_deposit": "收到对账消息，且实付大于定金应付",
    "unpaid_balance": "尾款结束15分钟后，已付定金未付尾款",  # 尾款结束15分钟后，已付定金未付尾款的订单变为此状态
    "unpaid_full_balance": "收到对账消息，且实付小于尾款应付",
    "excessive_balance": "收到对账消息，且实付大于尾款应付，对账类型为完全对账",
    "unpaid_full": "收到对账消息，且实付小于全款应付",
    "excessive_paid": "收到对账消息，且实付大于全款应付，对账类型为完全对账",
    "breach_contract": "商家违约",
    "paused": "订单暂停",  # 目前仅京东
    "locked": "订单锁定",  # 目前仅京东
    "group": "拼团成功",  # 目前仅pdd
    "paid": "已付款",
    "part_shipped": "部分发货",
    "shipped": "发货",
    "signed": "签收",  # 目前仅pdd
    "succeeded": "交易成功",
    "closed": "订单取消",
    "refund": "订单退款"  # 目前仅pdd
}

class OrderParams(BaseModel):
    platform: str
    order_id: str

@router.post("/get_order_info")
async def get_order_info(order_params: OrderParams) -> str:
    """
    获取订单信息
    
    Args:
        platform: 电商平台信息
        order_id: 订单ID
        
    Returns:
        订单信息的格式化字符串
    """
    # 生成缓存键
    _config = get_config()
    cache_key = get_md5(**order_params.model_dump())
    if _config["data"].get("cache"):
        cached_data = read_cache("get_order_info", cache_key)
        if cached_data:
            return cached_data
        else:
            return "没有查询到订单信息"
    
    # 格式化订单ID（添加前缀）
    order_id = "1000282702_" + str(order_params.order_id) if not order_params.order_id.startswith('1000282702_') else order_params.order_id
    
    # 获取API地址和头信息
    location, headers = center(order_params.platform, 'order')
    
    # 构建请求数据
    data = {"platform": order_params.platform, "order_id": str(order_id)}
    
    try:
        # 发送请求
        response = requests.post(location, headers=headers, json=data)
        
        if response.status_code == 200:
            result = response.json()
            order_info = result.get('order', {})
            
            try:
                # 提取订单信息
                address = order_info.get('address', '')
                address = f"此订单收货地址为{address}。\n"
                
                goods_id = order_info.get('item_ids', [''])[0]
                goods_id = f"此订单商品的商品ID为{goods_id}。\n"
                
                status = ORDER_STATUS_DICT.get(order_info.get("status_v2", ''), "未知")
                status = f"此订单目前状态为{status}。\n"
                
                order_information = address + goods_id + status
            except Exception:
                order_information = '未能查到此订单信息。'
        else:
            order_information = '未能查到此订单信息。'
    except Exception:
        order_information = '未能查到此订单信息。'
    
    # 将结果写入缓存
    write_cache("get_order_info", cache_key, order_information)
    return order_information