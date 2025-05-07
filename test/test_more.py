from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import initialize_agent
from langchain_community.chat_models import ChatZhipuAI
import os
import asyncio
from langgraph.prebuilt import create_react_agent
os.environ["ZHIPUAI_API_KEY"] = '2d00fac6fbc0408db8bd096b9b704a41.9Hje9rgehzpa22ku'

os.environ['LANGSMITH_TRACING']='true'
os.environ['LANGSMITH_ENDPOINT']="https://api.smith.langchain.com"
os.environ['LANGSMITH_API_KEY']="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"
os.environ['LANGSMITH_PROJECT']="pr-loyal-firewall-40"
LLM = ChatZhipuAI(
    model="glm-4-air-250414",
    temperature=0.3
)

async def init_tools():
    # 创建 MCP 工具实例
    async with MultiServerMCPClient(
    {
        "math": {
            "command": "python",
            # Replace with absolute path to your math_server.py file
            "args": ["/Users/utopia/Documents/晓多/Ebench/test/server_math.py"],
            "transport": "stdio",
        },
        "weather": {
            # Ensure your start your weather server on port 8000
            "command": "python",
            "args": ["/Users/utopia/Documents/晓多/Ebench/test/server_weather.py"],
            "transport": "stdio",
        }
    }
    ) as client:
        mcp_tool = client.get_tools()
        print("\n\n\n")
        print(mcp_tool)
        return client

async def main():
    client = await init_tools()
    print(client.get_tools())
    # 初始化代理
    agent = create_react_agent(
        LLM,
        client.get_tools(),
    )

    math_response = await agent.ainvoke(
    {"messages": [
        {"role": "system", "content": "用中文回复."},
        {"role": "user", "content": "what's (3 + 5) x 12?"}
        ]
    }
    )
    print("\n\n")
    print(math_response)
    print("\n\n")
    print(math_response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())