import uvicorn
from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from rich.console import Console
from api import router
from utils.config import get_config
import json
# 配置中间件
middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'], allow_methods=["GET", "POST", "PATCH", "PUT", "DELETE", "OPTIONS"])
]
console = Console()
# 创建FastAPI应用
app = FastAPI(middleware=middleware)

# 引入路由
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "API已启动"}

if __name__ == "__main__":
    config = get_config()
    console.print(f"[blue] {json.dumps(config, ensure_ascii=False, indent=2)}[/blue]")
    uvicorn.run(app, host=config["host"]["url"], port=config["host"]["port"])