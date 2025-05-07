import requests
from fastapi import APIRouter
from pydantic import BaseModel
from utils.config import get_config
from utils.cache import get_md5, read_cache, write_cache

# 创建路由
router = APIRouter()

class DiscountParams(BaseModel):
    platform: str
    shop_id: str
    order_id: str

@router.post("/get_discount_info")
async def get_discount_info(discount_params: DiscountParams) -> str:
    """
    获取优惠信息
    当用户询问优惠政策时，可以调用此函数
    
    Args:
        platform: 电商平台信息
        shop_id: 店铺ID
        order_id: 订单ID
        
    Returns:
        优惠信息的格式化字符串
    """
    # 生成缓存键
    _config = get_config()
    cache_key = get_md5(**discount_params.dict())
    if _config.get("cache") == "true":
        cached_data = read_cache("get_discount_info", cache_key)
        if cached_data is not None:
            return cached_data
        else:
            return "没有查询到优惠信息"
        
    # 这里应该是实际获取优惠信息的API调用
    # 由于原始代码中没有提供实际实现，这里我们模拟一个结果
    try:
        # 假设我们调用了某个API获取优惠信息
        discount_information = f"订单 {discount_params.order_id} 在 {discount_params.platform} 平台的店铺 {discount_params.shop_id} 有以下优惠:\n"
        discount_information += "1. 新用户首单立减10元\n"
        discount_information += "2. 满100减15元\n"
        discount_information += "3. 会员用户额外95折"
        
        # 将结果写入缓存
        write_cache("get_discount_info", cache_key, discount_information)
        
        return discount_information
    
    except Exception as e:
        error_msg = f"获取优惠信息失败: {str(e)}"
        return error_msg