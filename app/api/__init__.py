from fastapi import APIRouter
from .logistics import router as logistics_router
from .order import router as order_router
from .discount import router as discount_router
from .product import router as product_router

# 创建主路由
router = APIRouter()

# 注册子路由
router.include_router(logistics_router, tags=["logistics"])
router.include_router(order_router, tags=["order"])
router.include_router(discount_router, tags=["discount"])
router.include_router(product_router, tags=["product"])