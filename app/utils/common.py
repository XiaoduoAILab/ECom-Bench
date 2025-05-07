from typing import Tuple, Dict
from .config import get_config

def center(platform: str, center_type: str) -> Tuple[str, Dict[str, str]]:
    """
    根据平台和类型获取API的URL和请求头
    
    Args:
        platform: 平台名称，如'tb'、'jd'等
        center_type: API类型，如'logistics'、'order'等
        
    Returns:
        API的URL和请求头的元组
    """
    config = get_config()
    
    # 根据平台选择基础URL和认证信息
    if platform == 'tb':
        base_url = config["api"]["tb"]["base_url"]
        auth = config["api"]["tb"]["auth"]
    else:
        base_url = config["api"]["other"]["base_url"]
        auth = config["api"]["other"]["auth"]
    
    # 获取API路径
    if center_type not in config["api"]["paths"]:
        raise ValueError(f"不支持的API类型: {center_type}")
    
    path = config["api"]["paths"][center_type]
    location = base_url + path
    
    # 构建请求头
    headers = {'Content-type': 'application/json'}
    headers['Authorization'] = auth
    
    return location, headers

def format_order_id(platform: str, order_id: str) -> str:
    """
    根据平台格式化订单ID
    
    Args:
        platform: 平台名称
        order_id: 原始订单ID
        
    Returns:
        格式化后的订单ID
    """
    # 不同平台订单ID前缀处理
    prefixes = {
        'logistics': '1000282702_',
        'order': '1000001465_'
    }
    
    # 根据平台和类型添加前缀
    for prefix_type, prefix in prefixes.items():
        if prefix_type == 'logistics':
            if not order_id.startswith(prefix):
                return prefix + order_id
    
    return order_id

def format_buyer_id(buyer_id: str) -> str:
    """
    格式化买家ID，去除前缀
    
    Args:
        buyer_id: 原始买家ID
        
    Returns:
        格式化后的买家ID
    """
    if buyer_id:
        prefix = "cnjd"
        if buyer_id.startswith(prefix):
            return buyer_id[len(prefix):]
    
    return buyer_id