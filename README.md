
# Ecom-Bench: 电商客服对话评估基准测试框架
[![arXiv](https://img.shields.io/badge/Arxiv-2507.05639-b31b1b.svg?logo=arXiv)](https://arxiv.org/pdf/2507.05639)
[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/tatsu-lab/stanford_alpaca/blob/main/LICENSE)

## 概述

Ecom-Bench是一个专门用于评估电商客服对话系统性能的综合基准测试框架。该框架通过模拟真实的电商客服场景，为自然语言处理系统在实际工业环境中的部署提供了标准化的评估方法。<mcreference link="https://2025.emnlp.org/calls/industry_track/" index="1">1</mcreference> <mcreference link="https://2024.emnlp.org/calls/industry_track/" index="4">4</mcreference>

## 主要特性

### 🎯 真实场景模拟
- **多平台支持**: 支持京东等主流电商平台的客服场景
- **用户画像驱动**: 基于真实用户行为特征的用户模拟器
- **多轮对话**: 支持复杂的多轮对话交互评估

### 🤖 灵活的代理架构
- **多种用户策略**: 支持基于规则(based)、思维链(cot)和人工(human)的用户模拟
- **多种代理策略**: 支持LLM驱动和人工的客服代理
- **模型无关**: 支持多种大语言模型(Qwen、DeepSeek-V3等)

### 📊 全面的评估指标
- **动作准确性**: 评估客服执行的操作是否正确
- **搜索效率**: 评估信息检索的准确性和效率
- **输出质量**: 评估回复内容的质量和相关性
- **响应时间**: 评估系统的实时性能

### 🛠️ 工具集成
- **MCP协议支持**: 集成Model Context Protocol进行工具调用
- **异步处理**: 支持高并发的异步对话处理
- **结果缓存**: 智能缓存机制提升评估效率

## 安装要求

```bash
pip install -r requirements.txt
```

### 主要依赖
- `langchain-community>=0.3.23`
- `langchain-openai>=0.3.7`
- `langgraph>=0.3.2`
- `openai>=1.71.0`
- `rich` (用于美观的命令行输出)
- `pydantic` (用于数据验证)

## 快速开始

### 基本使用

```bash
# 运行单个试验
python run.py --env story --user-model qwen --agent-model qwen

# 运行多个试验
python run.py --num-trials 5 --env story

# 指定任务范围
python run.py --start-index 0 --end-index 10

# 运行特定任务
python run.py --task-ids 1 2 3
```

### 高级配置

```bash
# 自定义用户和代理策略
python run.py --user-strategy cot --agent-strategy llm

# 设置并发数和日志目录
python run.py --max-concurrency 5 --log-dir ./custom_results

# 启用详细输出
python run.py --verbose
```

## 项目结构

```
Ecom-Bench/
├── agent/                    # 代理实现
│   ├── agents_list/         # 不同类型的代理
│   │   ├── agent_human.py   # 人工代理
│   │   ├── agent_langchain.py # LangChain代理
│   │   └── agent_sdk.py     # SDK代理
│   └── servers/             # 服务器组件
├── envs/                    # 环境实现
│   ├── base.py             # 基础环境类
│   └── story/              # 故事场景环境
│       ├── env.py          # 环境逻辑
│       ├── tasks.py        # 任务定义
│       ├── wiki.md         # 用户指南
│       └── wiki.py         # Wiki处理
├── user/                    # 用户模拟器
│   ├── memory.py           # 记忆管理
│   └── user.py             # 用户实现
├── main.py                  # 主执行逻辑
├── run.py                   # 命令行接口
├── utils.py                 # 工具函数
└── requirements.txt         # 依赖列表
```

## 核心组件

### 环境系统
<mcfile name="env.py" path="/Users/utopia/Documents/晓多/Ecom-Bench/envs/story/env.py"></mcfile>实现了完整的电商客服对话环境，包括:
- 任务加载和管理
- 用户-代理交互循环
- 工具调用跟踪
- 性能指标计算

### 用户模拟器
<mcfile name="user.py" path="/Users/utopia/Documents/晓多/Ecom-Bench/user/user.py"></mcfile>提供了多种用户模拟策略:
- **UserBased**: 基于规则的用户行为模拟
- **UserCoT**: 基于思维链的用户推理
- **UserHuman**: 人工用户交互

### 代理系统
<mcfile name="agent_sdk.py" path="/Users/utopia/Documents/晓多/Ecom-Bench/agent/agents_list/agent_sdk.py"></mcfile>支持多种客服代理实现:
- 集成多个LLM提供商(Qwen、DeepSeek等)
- MCP工具调用支持
- 可配置的模型参数

## 评估指标

框架提供四个主要评估维度:

1. **动作准确性** (`reward_actions`): 评估代理执行的操作是否符合用户需求
2. **搜索质量** (`reward_searches`): 评估信息检索的准确性和相关性
3. **输出质量** (`reward_outputs`): 评估回复内容的质量和有用性
4. **时间效率** (`reward_time`): 评估系统响应时间和整体效率

## 任务配置

<mcfile name="tasks.py" path="/Users/utopia/Documents/晓多/Ecom-Bench/envs/story/tasks.py"></mcfile>包含了丰富的测试任务，每个任务包括:
- 用户画像(消费者类型、性格特征、行为特征)
- 具体的交互意图和目标
- 平台和商店信息
- 评估标准

## 实验配置

### 支持的模型
- **Qwen系列**: 通过阿里云DashScope API
- **DeepSeek-V3**: 通过火山引擎API
- **OpenAI系列**: 通过标准OpenAI API

### 配置参数
<mcfile name="utils.py" path="/Users/utopia/Documents/晓多/Ecom-Bench/utils.py"></mcfile>中的`RunConfig`类定义了所有可配置参数:
- 模型选择和策略配置
- 任务范围和并发设置
- 日志和输出配置
- 性能调优参数

## 结果分析

运行完成后，结果将保存为JSON格式，包含:
- 详细的对话轨迹
- 各维度的评分
- 工具调用记录
- 性能统计信息

使用<mcfile name="results2metrics.py" path="/Users/utopia/Documents/晓多/Ecom-Bench/results2metrics.py"></mcfile>可以进一步分析和可视化结果。

## 扩展性

### 添加新环境
1. 在`envs/`目录下创建新的环境模块
2. 继承`Env`基类并实现必要方法
3. 在`envs/__init__.py`中注册新环境

### 添加新代理
1. 在`agent/agents_list/`下实现新的代理类
2. 遵循现有的接口规范
3. 更新代理选择逻辑

### 添加新用户策略
1. 在`user/`目录下实现新的用户类
2. 实现`call`方法和系统提示加载
3. 在环境中注册新策略

## 贡献指南

我们欢迎社区贡献！请遵循以下步骤:
1. Fork本仓库
2. 创建特性分支
3. 提交更改
4. 创建Pull Request

## 许可证

本项目采用Apache 2.0许可证。详见LICENSE文件。

## 引用

如果您在研究中使用了Ecom-Bench，请引用:

```bibtex
@misc{Ecom-Bench2024,
  title={Ecom-Bench: A Comprehensive Benchmark for E-commerce Customer Service Dialogue Systems},
  author={[作者姓名]},
  year={2024},
  url={https://github.com/[用户名]/Ecom-Bench}
}
```

## 联系方式

如有问题或建议，请通过以下方式联系:
- 提交GitHub Issue
- 发送邮件至: [联系邮箱]

---

**注**: 本框架专为学术研究和工业应用设计，符合EMNLP Industry Track对真实世界应用和可重现研究的要求。<mcreference link="https://2025.emnlp.org/calls/industry_track/" index="1">1</mcreference> <mcreference link="https://2024.emnlp.org/calls/industry_track/" index="4">4</mcreference>
        
