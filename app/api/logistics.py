import requests
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from utils.common import center, format_order_id, format_buyer_id
from utils.cache import get_md5, read_cache, write_cache
from utils.config import get_config

# 创建路由
router = APIRouter()

class LogisticsParams(BaseModel):
    platform: str
    shop_id: str
    order_id: str
    buyer_id: Optional[str] = None

@router.post("/get_logistics_info")
async def get_logistics_info(logistics_params: LogisticsParams) -> str:
    """
    获取物流信息
    
    Args:
        platform: 电商平台信息
        shop_id: 店铺ID
        order_id: 订单ID
        buyer_id: 买家ID（可选）
        
    Returns:
        物流信息的格式化字符串
    """
    # 生成缓存键
    cache_key = get_md5(**logistics_params.model_dump())
    _config = get_config()
    if _config["data"].get("cache"):
        cached_data = read_cache("get_logistics_info", cache_key)
        if cached_data:
            return cached_data
        else:
            return "没有查询到物流信息"
    
    # 获取API地址和头信息
    location, headers = center(logistics_params.platform, 'logistics')
    order_id = logistics_params.order_id
    buyer_id = logistics_params.buyer_id
    # 格式化订单ID和买家ID
    order_id = "1000282702_" + order_id if not order_id.startswith('1000282702_') else order_id
    prefix = "cnjd"
    if buyer_id and buyer_id.startswith(prefix):
        buyer_id = buyer_id[len(prefix):]
        
    # 构建请求数据
    if logistics_params.platform == 'tb':
        payload = {
            "platform": logistics_params.platform,
            "order_id": order_id,
            "shop_id": logistics_params.shop_id,
        }
    else:
        payload = {
            "platform": logistics_params.platform,
            "order_id": order_id,
            "shop_id": logistics_params.shop_id,
            "order_type": 0,  # orderType只有京东平台有 0 表示京东自营，18 表示厂直 22 表示京东pop订单
            "buyer_id": buyer_id if buyer_id else None
        }
    
    try:
        # 发送请求
        response = requests.post(location, headers=headers, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            
            if result:
                # 处理物流信息列表
                logistics_info_list = result.get('logistics_list', [])
                prefix = f"该订单共有{len(logistics_info_list)}个物流信息：\n\n"
                logistics_information_list = ""
                
                if logistics_info_list:
                    for logistics_info in logistics_info_list:
                        # 获取物流单号
                        tracking_num = logistics_info.get('out_sid', '')
                        tracking_num = f"物流单号为{tracking_num}。\n"
                        
                        # 获取物流公司
                        logistics_company = logistics_info.get('company_name', '')
                        logistics_company = f"物流公司为{logistics_company}。\n"
                        
                        # 获取物流状态
                        logistics_status = logistics_info.get('status', '')
                        logistics_status = f"当前物流状态为{logistics_status}。\n"
                        
                        # 获取物流步骤
                        logistics_steps = logistics_info.get('steps', '')
                        if logistics_steps:
                            steps = '\n'.join([f"{step['status_time']}：{step['status_desc']}" for step in logistics_steps])
                            steps = f"物流明细为：\n{steps}"
                        else:
                            steps = "无物流明细"
                            
                        logistics_information = f"{tracking_num}{logistics_company}{logistics_status}{steps}\n\n"
                        logistics_information_list += logistics_information
                        
                    logistics_information_list_str = prefix + logistics_information_list
                else:
                    logistics_information_list_str = "未能查到此订单物流信息。"
            else:
                logistics_information_list_str = "未能查到此订单物流信息。"
        else:
            logistics_information_list_str = "未能查到此订单物流信息。"
    except Exception as e:
        logistics_information_list_str = "未能查到此订单物流信息。"

    # 将结果写入缓存
    write_cache("get_logistics_info", cache_key, logistics_information_list_str)
    
    return logistics_information_list_str