# Ecom-Bench: E-commerce Customer Service Dialogue Evaluation Benchmark Framework
[![arXiv](https://img.shields.io/badge/Arxiv-2507.05639-b31b1b.svg?logo=arXiv)](https://arxiv.org/pdf/2507.05639)
[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-blue.svg)](https://github.com/tatsu-lab/stanford_alpaca/blob/main/LICENSE)

<h4 align="center">
    <p>
        <a href="https://github.com/XiaoduoAILab/ECom-Bench/blob//main/README_CN.md">中文</a> | <b>English</b>
    <p>
</h4>

## Project Background
Developed based on the tau-bench project with special thanks to Sierra Inc. for their open-source contribution  
tau-bench uses MIT license: [View details](https://github.com/sierra-research/tau-bench/blob/main/LICENSE)

## Important Notice
⚠️ This simulation environment contains simulated user data for non-production testing only  
🛡️ Strictly prohibited for training with real user data, fully compliant with China's Personal Information Protection Law (PIPL)

## Framework Positioning
Ecom-Bench is a comprehensive evaluation benchmark framework designed for e-commerce customer service dialogue systems, providing standardized validation solutions through real-world scenario simulations before industrial deployment of natural language processing systems.

### Core Advantages
![images/table1.png](https://github.com/XiaoduoAILab/ECom-Bench/blob/main/images/table1.png)

🎯 **Realistic Scenario Recreation**  
- Supports reproduction of customer service scenarios from mainstream platforms like JD.com
- User profile-driven based on real user behavior characteristics
- Complex multi-turn dialogue interaction verification

🤖 **Flexible Architecture Design**  
- User strategies: Rule-based/Based, Chain-of-Thought (CoT), Human-in-the-loop
- Agent strategies: LLM-driven/Dual-mode (human + AI)
- Model-agnostic: Compatible with mainstream large models like Qwen, DeepSeek-V3

📊 **Multi-dimensional Evaluation System**  
| Dimension          | Core Metrics                 |
|--------------------|------------------------------|
| Action Accuracy    | Operation command execution accuracy |
| Search Efficiency  | Information retrieval precision     |
| Output Quality     | Response content relevance         |
| Response Timeliness| System real-time responsiveness    |

🛠️ **Engineering Support**
- Native support for MCP (Model Context Protocol) tool calling protocol
- Asynchronous high-concurrency dialogue processing engine
- Smart result caching for accelerated evaluation

## Installation Requirements

```bash
pip install -r requirements.txt
```

### Main Dependencies
- `langchain-community>=0.3.23`
- `langchain-openai>=0.3.7`
- `langgraph>=0.3.2`
- `openai>=1.71.0`
- `rich` (for beautiful command-line output)
- `pydantic` (for data validation)

## Quick Start

### Basic Usage

```bash
# Run single trial
python run.py --env story --user-model qwen --agent-model qwen

# Run multiple trials
python run.py --num-trials 5 --env story

# Specify task range
python run.py --start-index 0 --end-index 10

# Run specific tasks
python run.py --task-ids 1 2 3
```

### Advanced Configuration

```bash
# Custom user and agent strategies
python run.py --user-strategy cot --agent-strategy llm

# Set concurrency and log directory
python run.py --max-concurrency 5 --log-dir ./custom_results

# Enable verbose output
python run.py --verbose
```

## System Architecture

```
Ecom-Bench/
├── agent/                    # Agent implementation
│   ├── agents_list/         # Different agent types
│   │   ├── agent_human.py   # Human agent
│   │   ├── agent_langchain.py # LangChain agent
│   │   └── agent_sdk.py     # SDK agent
│   └── servers/             # Server components
├── envs/                    # Environment implementation
│   ├── base.py             # Base environment class
│   └── story/              # Story scenario environment
│       ├── env.py          # Environment logic
│       ├── tasks.py        # Task definitions
│       ├── wiki.md         # User guide
│       └── wiki.py         # Wiki processing
├── user/                    # User simulator
│   ├── memory.py           # Memory management
│   └── user.py             # User implementation
├── main.py                  # Main execution logic
├── run.py                   # Command-line interface
├── utils.py                 # Utility functions
└── requirements.txt         # Dependency list
```
![images/figure1.png](https://github.com/XiaoduoAILab/ECom-Bench/blob/main/images/figure1.png)
## Core Components

### Environment System
<mcfile name="env.py" path="/Users/utopia/Documents/晓多/Ecom-Bench/envs/story/env.py"></mcfile>
implements a complete e-commerce customer service dialogue environment including:

- Task loading and management

- User-agent interaction loop

- Tool call tracking

- Performance metric calculation

### User Simulator
<mcfile name="user.py" path="/Users/utopia/Documents/晓多/Ecom-Bench/user/user.py"></mcfile> 
provides multiple user simulation strategies:

- UserBased: Rule-driven user behavior

- UserCoT: Chain-of-Thought reasoning user

- UserHuman: Human interaction interface

### Agent System
<mcfile name="agent_sdk.py" path="/Users/utopia/Documents/晓多/Ecom-Bench/agent/agents_list/agent_sdk.py"></mcfile> 
supports multiple customer service agent implementations:

- Integration with multiple LLM providers (Qwen, DeepSeek, etc.)

- Support for MCP tool calling

- Configurable model parameters

## Evaluation Metrics

The framework provides four main evaluation dimensions:

1. **Action Accuracy** (`reward_actions`): Evaluates whether agent-executed operations meet user requirements
2. **Search Quality** (`reward_searches`): Evaluates accuracy and relevance of information retrieval
3. **Output Quality** (`reward_outputs`): Evaluates quality and usefulness of responses
4. **Time Efficiency** (`reward_time`): Evaluates system response time and overall efficiency

## Task Configuration

<mcfile name="tasks.py" path="/Users/utopia/Documents/晓多/Ecom-Bench/envs/story/tasks.py"></mcfile> contains rich test tasks, each including:


&emsp;📌 User profile (consumption habits/personality traits)

&emsp;🎯 Interaction intent and goals

&emsp;🏬 Platform/store context information

&emsp;✅ Expected action acceptance criteria

## Experiment Configuration

### Supported Models
- **Qwen Series**: Calls AliCloud DashScope API

- **DeepSeek-V3**: Calls Volcano Engine API

- **OpenAI Series**: Calls standard OpenAI API

### Configuration Parameters
<mcfile name="utils.py" path="/Users/utopia/Documents/晓多/Ecom-Bench/utils.py"></mcfile> RunConfig class defines all configurable parameters:

- Model selection and strategy configuration

- Task range and concurrency settings

- Logging and output configuration

- Performance tuning parameters

## Result Analysis

After execution, results are saved in JSON format containing:

- Detailed dialogue trajectories

- Dimension-specific scores

- Tool call records

- Performance statistics

Use <mcfile name="results2metrics.py" path="/Users/utopia/Documents/晓多/Ecom-Bench/results2metrics.py"></mcfile> for further analysis and visualization.
## Extensibility

### Adding New Environments
1. Create new environment module under `envs/`

2. Inherit `Env` base class and implement required methods

3. Register new environment in `envs/__init__.py`

### Adding New Agents
1. Implement new agent class under `agent/agents_list/`

2. Follow existing interface specifications

3. Update agent selection logic

### Adding New User Strategies
1. Implement new user class under `user/`

2. Implement call method and system prompt loading

3. Register new strategy in environment

## License

This project uses Apache 2.0 license. See [LICENSE](https://github.com/XiaoduoAILab/ECom-Bench/blob/main/LICENSE)。

## Citation

If you use Ecom-Bench in your research, please cite:

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

## Contact

For questions or suggestions:

- Submit GitHub Issue

- Email: huangyizhe@xiaoduotech.com

---
