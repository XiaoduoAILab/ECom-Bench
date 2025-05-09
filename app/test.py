import httpx
import json

# FastAPI应用的主机地址
API_URL = "http://127.0.0.1:8000"  # 你可以根据你的配置修改这个URL

# 定义各路由的参数
discount_params = {
    "platform": "jd",
    "shop_id": "5de650c946e7c3001814990f",
    "order_id": "order123"
}

logistics_params = {
    "platform": "jd",
    "shop_id": "5de650c946e7c3001814990f",
    "order_id": "304656322378",
    "user_id": "cnjdjd_42f3b413bf221"
}

order_params = {
    "platform": "jd",
    "order_id": "310305074915"
}

product_params = {
    "platform": "jd",
    "shop_id": "5de650c946e7c3001814990f",
    "goods_id": "100192762770"
}

async def test_api():
    async with httpx.AsyncClient() as client:
        # 测试 /get_discount_info 路由
        response = await client.post(f"{API_URL}/get_discount_info", json=discount_params)
        print("Discount Info:\n", response.status_code, "\n", response.text)
        print("-" * 50)
        # 测试 /get_logistics_info 路由
        response = await client.post(f"{API_URL}/get_logistics_info", json=logistics_params)
        print("Logistics Info:\n", response.status_code, "\n", response.text)
        print("-" * 50)
        # 测试 /get_order_info 路由
        response = await client.post(f"{API_URL}/get_order_info", json=order_params)
        print("Order Info:\n", response.status_code, "\n", response.text)
        print("-" * 50)
        # 测试 /get_goods_property 路由
        response = await client.post(f"{API_URL}/get_goods_property", json=product_params)
        print("Product Info:\n", response.status_code, "\n", response.text)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_api())
