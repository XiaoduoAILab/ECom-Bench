import imp
import uvicorn
from fastapi import FastAPI
import yaml
import os
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from typing import List, Dict, Any, Tuple

with open(os.path.join(os.path.dirname(__file__), "config.yaml")) as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

cache = config["data"]["cache"]
cache_data_path = config["data"]["directory"]

middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'], allow_methods = ["GET", "POST", "PATCH", "PUT", "DELETE", "OPTIONS"])
]

app = FastAPI(middleware=middleware)
@app.post("/get_image_info")
async def get_image_info(summarized_query: str, history_messages: List[Dict]):
    return "get_image_info"


if __name__ == "__main__":
    uvicorn.run(app, host=config["host"]["url"], port=config["host"]["port"])