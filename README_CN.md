# Ecom-Bench：电商客服对话评估基准测试框架
[![arXiv](https://img.shields.io/badge/Arxiv-2507.05639-b31b1b.svg?logo=arXiv)](https://arxiv.org/pdf/2507.05639)
[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-blue.svg)](https://github.com/tatsu-lab/stanford_alpaca/blob/main/LICENSE)

<h4 align="center">
    <p>
        <b>中文</b> | <a href="https://github.com/XiaoduoAILab/ECom-Bench/blob/main/README.md">English</a>
    <p>
</h4>

## 项目背景
基于 tau-bench 项目开发，在此特别致谢 Sierra Inc. 的开源贡献  
tau-bench 采用 MIT 许可：[查看详情](https://github.com/sierra-research/tau-bench/blob/main/LICENSE)

## 重要声明
⚠️ 本仿真环境包含模拟用户数据，仅限非生产环境测试  
🛡️ 禁止用于真实用户数据训练，严格遵循《个人信息保护法》要求

## 框架定位
Ecom-Bench 是专为电商客服对话系统设计的综合评估基准测试框架，通过真实场景模拟为自然语言处理系统提供工业级部署前的标准化验证方案。

### 核心优势
![images/table1.png](https://github.com/XiaoduoAILab/ECom-Bench/blob/main/images/table1.png)

🎯 **真实场景还原**  
- 支持京东等主流电商平台客服场景复现
- 基于真实用户行为特征的用户画像驱动
- 复杂多轮对话交互能力验证

🤖 **灵活架构设计**  
- 用户策略：规则驱动(based)/思维链(cot)/人工介入(human)
- 客服策略：LLM驱动/人工双模式
- 模型无关：兼容 Qwen、DeepSeek-V3 等主流大模型

📊 **多维评估体系**  
| 评估维度       | 核心指标               |
|----------------|------------------------|
| 动作准确性     | 操作指令执行正确率     |
| 搜索效率       | 信息检索精准度         |
| 输出质量       | 回复内容相关性         |
| 响应时效       | 系统实时响应能力       |

🛠️ **工程化支持**
- 原生支持 MCP(Model Context Protocol)工具调用协议
- 异步高并发对话处理引擎
- 智能结果缓存加速评估流程

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
# 自定义用户和智能体策略
python run.py --user-strategy cot --agent-strategy llm

# 设置并发数和日志目录
python run.py --max-concurrency 5 --log-dir ./custom_results

# 启用详细输出
python run.py --verbose
```

## 系统架构

```
Ecom-Bench/
├── agent/                    # 智能体实现
│   ├── agents_list/         # 不同类型的智能体
│   │   ├── agent_human.py   # 人工智能体
│   │   ├── agent_langchain.py # LangChain智能体
│   │   └── agent_sdk.py     # SDK智能体
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
![images/figure1.png](https://github.com/XiaoduoAILab/ECom-Bench/blob/main/images/figure1.png)
## 核心组件

### 环境系统
<mcfile name="env.py" path="/Users/utopia/Documents/晓多/Ecom-Bench/envs/story/env.py"></mcfile>实现了完整的电商客服对话环境，包括:
- 任务加载和管理
- 用户-代理交互循环
- 工具调用跟踪
- 性能指标计算

### 用户模拟器
<mcfile name="user.py" path="/Users/utopia/Documents/晓多/Ecom-Bench/user/user.py"></mcfile>提供了多种用户模拟策略:
- **UserBased**: 规则驱动型用户行为
- **UserCoT**: 思维链推理型用户
- **UserHuman**: 人工交互接口

### 智能体系统
<mcfile name="agent_sdk.py" path="/Users/utopia/Documents/晓多/Ecom-Bench/agent/agents_list/agent_sdk.py"></mcfile>支持多种客服智能体实现:
- 集成多个LLM提供商(Qwen、DeepSeek等)
- 支持MCP工具调用
- 可配置模型参数

## 评估指标

框架提供四个主要评估维度:

1. **动作准确性** (`reward_actions`): 评估代理执行的操作是否符合用户需求
2. **搜索质量** (`reward_searches`): 评估信息检索的准确性和相关性
3. **输出质量** (`reward_outputs`): 评估回复内容的质量和有用性
4. **时间效率** (`reward_time`): 评估系统响应时间和整体效率

## 任务配置

<mcfile name="tasks.py" path="/Users/utopia/Documents/晓多/Ecom-Bench/envs/story/tasks.py"></mcfile>包含了丰富的测试任务，每个任务包括:


&emsp;📌 用户画像（消费习惯/性格特征）

&emsp;🎯 交互意图与目标

&emsp;🏬 平台店铺上下文信息

&emsp;✅ 预期动作验收标准

## 实验配置

### 支持的模型
- **Qwen系列**: 调用阿里云DashScope API
- **DeepSeek-V3**: 调用火山引擎API
- **OpenAI系列**: 调用标准OpenAI API

### 配置参数
<mcfile name="utils.py" path="/Users/utopia/Documents/晓多/Ecom-Bench/utils.py"></mcfile>`RunConfig`类定义了所有可配置参数:
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

### 添加新智能体
1. 在`agent/agents_list/`下实现新的代理类
2. 遵循现有的接口规范
3. 更新代理选择逻辑

### 添加新用户策略
1. 在`user/`目录下实现新的用户类
2. 实现`call`方法和系统提示加载
3. 在环境中注册新策略

## 许可证

本项目采用Apache 2.0许可证。详见[LICENSE](https://github.com/XiaoduoAILab/ECom-Bench/blob/main/LICENSE)。

## 引用

如果您在研究中使用了Ecom-Bench，请引用:

```bibtex
@misc{wang2025ecombenchllmagentresolve,
      title={ECom-Bench: Can LLM Agent Resolve Real-World E-commerce Customer Support Issues?}, 
      author={Haoxin Wang and Xianhan Peng and Xucheng Huang and Yizhe Huang and Ming Gong and Chenghan Yang and Yang Liu and Ling Jiang},
      year={2025},
      eprint={2507.05639},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2507.05639}, 
}
```

## 联系方式

如有问题或建议，请通过以下方式联系:
- 提交GitHub Issue
- 发送邮件至: huangyizhe@xiaoduotech.com

---

        
