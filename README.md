# 项目目录

```
.
├── main.py                # 主程序入口
├── run.py                 # 运行入口
├── utils.py               # 全局工具函数
│
├── agent/                 # 智能代理模块
│   ├── agent.py           # 代理核心逻辑
│   ├── server.py          # 代理服务端
│   └── tools/             # 代理工具集
│       ├── apis/          # API接口模块
│       │   ├── console/   # 控制台接口
│       │   └── models/    # 模型接口
│       │       ├── azure_openai.py
│       │       ├── deepseek_v3_model.py
│       │       ├── doubao_model.py
│       │       └── ...    # 其他模型实现
│       ├── config.py      # 工具配置
│       ├── config.yaml    # 工具配置文件
│       └── get_*.py       # 各种信息获取工具
│
├── app/                   # 应用服务模块
│   ├── fastapi_service.py # FastAPI服务入口
│   ├── api/               # API接口
│   │   ├── discount.py
│   │   ├── logistics.py
│   │   ├── order.py
│   │   └── product.py
│   ├── utils/             # 应用工具
│   │   ├── cache.py
│   │   ├── common.py
│   │   └── config.py
│   └── data/              # 应用数据
│
├── envs/                  # 环境模块
│   ├── base.py            # 基础环境
│   ├── online/            # 在线环境
│   │   ├── env.py
│   │   ├── tasks.py
│   │   └── wiki.md
│   ├── reward.py          # 奖励环境
│   └── story/             # 故事环境
│
├── test/                  # 测试模块
│   ├── server_*.py        # 各种测试服务
│   └── test_*.py         # 测试用例
│
├── user/                  # 用户模块
│   ├── user.py            # 用户管理
│   ├── memory.py          # 记忆管理
│   └── tools/             # 用户工具
│
└── wikis/                 # 文档资料
    ├── agent_wiki.md      # 代理文档
    └── reward_wiki.md     # 奖励文档
```

# 运行命令
python run.py ：运行主程序。 # python run.py --env story --task-ids 0 --verbose
cd app && python fastapi_service.py ：运行FastAPI服务。