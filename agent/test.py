import os
import sys
import asyncio
import json
from rich.console import Console
# 添加父目录到路径以启用本地导入
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 本地导入
from agent import Agent
from langchain_mcp_adapters.client import MultiServerMCPClient

# 获取基础目录
base_dir = os.path.dirname(os.path.abspath(__file__))
console = Console()
# 定义系统提示
system_prompt = '''
# 基本信息
你现在是一名电商客服，你所属的平台是{platform}，你的商铺的shop_id是{shop_id}，你所服务的顾客的user_id是{user_id}。

# 基本行为
- 作为电商客服，你需要满足用户的需求
- 在不确定的时候，优先使用工具进行调用获得信息然后回复。
- 禁止使用英文回复，全部使用中文进行回复。
- 记住，参数不要换，获得什么参数，工具调用就使用什么参数，不要修改。
- 任务1：结合历史上下文中的买家问题，聚焦分析最新一次用户输入中的问题总结买家需求。如果无明显问题，则从历史上下文中最后一句买家发送的消息中寻找。
- 任务2：根据任务1得到的顾客需求，自行决定调用什么工具获取信息
- 任务3：根据要求找到的答案推理出能回答任务1的答案，针对顾客的需求进行回答。
- 任务4：买家问题涉及订单信息时如果没有查询到和用户问句相关的内容，回复只输出"没有该商品订单信息"一种回答；买家问题涉及物流信息时如果没有查询到和用户问句相关的内容，回复只输出"没有该商品物流信息"一种回答；买家问题涉及商品信息时如果没有查询到和用户问句相关的内容，回复只输出"没有该商品参数信息"一种回答；有相关内容时，礼貌尊称顾客为"小主xx"语言风格以专业电商客服聊天风格输出，语气亲切。
- 回复要求1：回复时只回复返回信息中有确定依据的内容，如果上述所有信息中无确定依据的情况下坚决只选择以下3个回复："没有该商品订单信息"，"没有该商品物流信息"，"没有该商品参数信息"作为回答。
- 回复要求2：回复时使用中性词语，禁止使用极限词。
- 回复要求3：在被问及是否刺激时，需要回复"具体看个人感觉哦"或者"因人而异"的说法。即使商品属性中提及不刺激。
- 回复要求4：回复简洁明了，每条不超过50字。
- 请参考当前问句和提供的订单，物流，商品参数等信息以及历史对话信息，对买家当前问句做出回复。
'''


async def main():
    """运行电商客服代理的主函数。"""
    async with MultiServerMCPClient({
        "service": {
            "command": "python",
            "args": [os.path.join(base_dir, "server.py")],
            "transport": "stdio",
        }
    }) as client_service:
        # 定义客户和商铺信息
        user_id = "cnjdjd_42f3b413bf221"
        shop_id = "5de650c946e7c3001814990f"
        platform = "jd"
        
        # 初始化代理并加载系统提示
        agent = Agent(
            agent_model="deepseek-v3", 
            mcp_tools=client_service.get_tools()
        )
        agent.load_system_prompt(
            system_prompt.format(
                user_id=user_id, 
                shop_id=shop_id, 
                platform=platform
            )
        )
        
        # 示例用户消息（包含图片URL）
        msg = '''
        帮我查询下这个订单 310305074915 的订单信息
        '''
        import requests
        # response = requests.post("http://localhost:8000/get_logistics_info", json={"platform": platform, "shop_id": shop_id, "order_id": "304656322378", "user_id": user_id})
        # print(response.json())
        # exit()
        
        # 获取代理响应并打印
        response = await agent.call(msg)
        details = [d.model_dump() for d in agent.detail_messages[0]]
        console.print(f"[bold blue]{json.dumps(details, ensure_ascii=False, indent=4)}")
        
        # print(response)


if __name__ == "__main__":
    asyncio.run(main())