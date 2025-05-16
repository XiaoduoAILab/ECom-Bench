#!/bin/bash

# 启动 FastAPI 服务（在 screen 会话中）
screen -dmS fastapi_service bash -c "cd app && python fastapi_service.py"

# 运行主任务
python run.py --env story --task-ids 0 --verbose