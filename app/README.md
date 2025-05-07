# 项目目录结构

```
.
├── fastapi_service.py     # FastAPI服务主入口文件
├── config.yaml            # 配置文件
├── api/                   # API接口模块
│   ├── __init__.py
│   ├── logistics.py       # 物流相关接口
│   ├── order.py           # 订单相关接口
│   ├── product.py         # 产品相关接口
│   └── discount.py        # 优惠相关接口
├── utils/                 # 工具模块
│   ├── __init__.py
│   ├── config.py          # 配置加载
│   ├── cache.py           # 缓存管理
│   └── common.py          # 公共工具函数
├── data/                  # 数据存储目录
└── test.py                # 测试文件
```

# 备注
是用的时候记得开VPN