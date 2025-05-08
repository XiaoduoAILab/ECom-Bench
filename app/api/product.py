import requests
import traceback
import asyncio
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from utils.common import center
from utils.cache import get_md5, read_cache, write_cache
from utils.config import get_config
import json
# 创建路由
router = APIRouter()

class ProductParams(BaseModel):
    platform: str
    shop_id: str
    goods_id: str

@router.post("/get_goods_property")
async def get_goods_property(product_params: ProductParams) -> str:
    """
    获取商品属性信息
    
    Args:
        platform: 电商平台信息
        shop_id: 店铺ID
        goods_id: 商品ID
        
    Returns:
        商品信息的格式化字符串
    """
    # 生成缓存键
    cache_key = get_md5(**product_params.model_dump())
    _config = get_config()
    if _config["data"].get("cache"):
        cached_data = read_cache("get_goods_property", cache_key)
        if cached_data:
            return cached_data
        else:
            return "没有查询到商品信息"

    # 并发获取两个渠道的商品信息
    try:
        # 使用asyncio.gather并发执行两个请求
        # 获取参数
        platform = product_params.platform
        shop_id = product_params.shop_id
        goods_id = product_params.goods_id
        
        # 并发请求
        shop_center_result, cube_result = await asyncio.gather(
            get_goods_info_shop_center(platform, shop_id, goods_id),
            get_goods_info_cube(platform, shop_id, goods_id)
        )
        
        # 解析shop_center结果
        shop_knowledge = format_goods_info_from_shop_center(shop_center_result)
        
        # 解析cube结果
        goods_knowledge = cube_result
        
        # 构建结果
        
        result = {
            "来自知立方商品知识库的商品信息：": goods_knowledge,
            **shop_knowledge
        }
        result = json.dumps(result, ensure_ascii=False, indent=2)
        write_cache("get_goods_property", cache_key, result)
            
        return result
        
    except Exception as e:
        error_msg = f"获取商品信息失败: {str(e)}\n{traceback.format_exc()}"
        return error_msg
    



async def get_goods_info_shop_center(platform: str, shop_id: str, plat_goods_id: str):
    # 调用官方center函数获取url和headers (新增)
    url, headers = center(platform, 'product')
        
    if platform == 'tb':
        data = {
            "platform": platform,
            "shop_id": str(shop_id),
            "plat_goods_id": str(plat_goods_id),
            "select": ["id", "plat_goods_name", "plat_goods_url", "article_number", "props", "status"]
        }
    elif platform == 'jd':
        data = {
            "platform": platform,
            "shop_id": str(shop_id),
            "plat_goods_id": str(plat_goods_id),
            "select": ["plat_goods_name", "plat_goods_url", "props", "status"]
        }
    elif platform == 'pdd':
        data = {
            "platform": platform,
            "shop_id": str(shop_id),
            "plat_goods_id": str(plat_goods_id),
            "return_fields_select": ["plat_goods_name", "plat_goods_url", "props", "status"]
        }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        data = result.get('data')
        if data and 'list' in data and data['list']:
            plat_goods_name = data['list'][0].get('plat_goods_name', "")
            plat_goods_url = data['list'][0].get('plat_goods_url', "")
            plat_goods_prop = data['list'][0].get('props', "")
            plat_goods_status = data['list'][0].get('status', "")
            plat_goods_custom_props = data['list'][0].get('custom_props', "")
        else:
            plat_goods_name = None
            plat_goods_url = None
            plat_goods_prop = None
            plat_goods_status = None
            plat_goods_custom_props = None
    else:
        plat_goods_name = None
        plat_goods_url = None
        plat_goods_prop = None
        plat_goods_status = None
        plat_goods_custom_props = None

    return plat_goods_name, plat_goods_url, plat_goods_prop, plat_goods_status, plat_goods_custom_props

async def get_goods_info_cube(platform, shop_id, goods_id):
    url = 'https://gateway.xiaoduoai.com/open/knowledge-goods/provider/goods_detail/get'
    # todo 有效期1年 2025/04/01-2026/04/01 'Basic aW50ZXJuYWxVc2VyOjcyQ0IwMDdEMzNFNjc0RURBRUE1QTAxRkUxMTI1MTcy',
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic aW50ZXJuYWxVc2VyOjcyQ0IwMDdEMzNFNjc0RURBRUE1QTAxRkUxMTI1MTcy',
    }
    data = {
        "shop_id": str(shop_id),
        "plat_goods_id": str(goods_id),
        "platform": str(platform)
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        try:
            data = response.json()
            goods_knowledge = data["data"][0].get("goods_detail_knowledge", "")
        except:
            goods_knowledge = '知立方知识库无商品信息'
    else:
        goods_knowledge = '知立方知识库无商品信息'
    return goods_knowledge


def format_goods_info_from_shop_center(shop_center_result):
    # 解析shop_center结果
    (plat_goods_name, plat_goods_url,
    plat_goods_prop, plat_goods_status,
    plat_goods_custom_props) = shop_center_result
    
    # 如果plat_goods_prop存在，则格式化输出
    if plat_goods_prop:
        plat_goods_prop_str = "\n".join(
            f"{item['prop_name']}：{','.join(item['value'])}" for item in plat_goods_prop)
    else:
        plat_goods_prop_str = '无商品信息'
        
    # 如果存在自定义属性，格式化输出
    if plat_goods_custom_props:
        plat_goods_custom_prop_str = "\n".join(
            f"{item['custom_prop']}：{','.join(item['value'])}" for item in plat_goods_custom_props)
    else:
        plat_goods_custom_prop_str = '无商品信息'
    
    return {
        "来自人工自定义的商品信息：": plat_goods_custom_prop_str,
        "来自商品中心的商品信息：": plat_goods_prop_str,
    }