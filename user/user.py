from utils import LLM

class UserBased(LLM):
    def __init__(self, user_model:str, verbose=False, mcp_tools= [], temperature = 0.3):
        super().__init__(model_name=user_model, verbose=verbose, mcp_tools=mcp_tools, temperature = 0.3)
        self.detail_messages = []
        self.user_model = super()._initiate_agent()
    
    
    def load_system_prompt(self, system_prompt):
        self.messages.append({"role": "system", "content": system_prompt})
    
    
    async def call(self, message:str) -> str:
        self.messages.append({"role": "user", "content": message})
        responses = await self.user_model.ainvoke(
            {
                "messages": self.messages
            },
            debug=self.verbose
        )
        self.detail_messages.append(responses["messages"])
        self.messages.append({"role": "assistant", "content": responses["messages"][-1].content})
        return responses["messages"][-1].content


from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import List
import json

class Think(BaseModel):
    '''分析之前的对话历史'''
    history:str = Field(...,description='你作为顾客已表达的需求和情绪')
    solution:str = Field(...,description='客服已提供的信息和解决方案')
    stage:str = Field(...,description='目前对话进展到哪个阶段')

class Intent(BaseModel):
    '''根据之前的对话历史确定你当前的主要意图'''
    emotion:str = Field(...,description='你当前的情绪状态如何')
    demand:str = Field(...,description='你目前的核心需求是什么')
    


class Evaluate(BaseModel):
    '''评估反应的合理性'''
    reaction:str = Field(...,description='需要评估的反应')
    consistency:str = Field(...,description='分析反应与你的角色设定是否一致')
    coherence:str = Field(...,description='分析每种反应与当前对话进展是否协调')
    realism:str = Field(...,description='分析每种反应是否符合真实顾客的自然反应')
    effectiveness:str = Field(...,description='分析反应是否有助于对话的继续和问题的解决，避免陷入僵持局面')
    

class Stop(BaseModel):
    '''判断是否需要停止对话'''
    reason:str = Field(...,description='是否需要停止对话的理由，例如所有意图完成，对话已经接近结束，此时必须选择停止对话。')
    stop:bool = Field(...,description='是否需要停止对话')

class Step(BaseModel):
    '''判断是否需要主动引导话题，转移到下一个意图'''
    count:int = Field(...,description='在同一个意图中已经讨论的次数')
    reason:str = Field(...,description='是否需要转移到下一个意图的理由，例如1.当客服满足不了你本次的需求 2.已经陷入僵持 3. 同一个意图讨论的次数大于1轮，需要转移到下一个意图。')
    step:bool = Field(...,description='是否需要转移到下一个意图')


class Response(BaseModel):
    '''内部思考框架（每次回复前都需执行）, 在生成每条顾客回复前，请先进行以下思考步骤'''
    think:Think = Field(...,description='分析之前的对话历史')
    stop:Stop = Field(...,description='判断是否需要停止对话')
    step:Step = Field(...,description='判断是否需要主动引导话题，转移到下一个意图、话题')
    intent:Intent = Field(...,description='根据之前的对话历史确定你当前的主要意图')
    reactions:List[str] = Field(...,description='基于自己的画像和背景,结合think、stop、step、intent的内容,生成不同的可能顾客反应')
    evaluates:List[Evaluate] = Field(...,description='一一评估每个反应的合理性，并给出对应的理由')
    final_response:str = Field(...,description='根据评估的结果选择最符合当前场景的反应方式，优先考虑有利于推进对话')
    
    
class UserCoT(UserBased):
    def __init__(self, user_model:str, verbose=False, mcp_tools= [], temperature = 0.3):
        super().__init__(user_model=user_model, verbose=verbose, mcp_tools=mcp_tools, temperature = 0.3)
        self.parser = PydanticOutputParser(pydantic_object=Response)
        self.prompt_template = PromptTemplate(
            template="""
# 这是客服的回复:
{solution}

# 这是你的背景信息: 
{character}

# 这是历史对话记录:
{history}

# 输出格式:
{format_instructions}   
            """,
            input_variables=["solution", "character", "history"],
            partial_variables={
                "format_instructions": self.parser.get_format_instructions()
            }
        )
    
    def load_system_prompt(self, system_prompt):
        self.system_prompt = system_prompt
        
    async def call(self, message:str) -> str:
        prompt = self.prompt_template.format_prompt(
            solution=message,
            character = self.system_prompt,
            history = self.messages,
        )
        responses = await self.user_model.ainvoke(
            {
                "messages": {
                    "role": "user",
                    "content": prompt.to_string()
                }
            },
            debug=self.verbose
        )
        self.detail_messages.append(responses["messages"])
        response = self.parser.parse(responses["messages"][-1].content)
        final_response = response.final_response
        stop = response.stop.stop
        if stop :
            final_response = '###STOP###'
        
        self.messages.append(f"客服回复: {message}")
        self.messages.append(f"你的回复：{final_response}")
        return final_response


class UserHuman(LLM):
    def __init__(self, user_model:str, verbose=False, mcp_tools= []):
        super().__init__(model_name=user_model, verbose=verbose, mcp_tools=mcp_tools)
        self.detail_messages = []
        self.user_model = super()._initiate_agent()
    
    def load_system_prompt(self, system_prompt):
        self.messages.append({"role": "system", "content": system_prompt})
    
    
    async def call(self, message:str) -> str:
        self.messages.append({"role": "user", "content": message})
        response = input("请输入你（顾客）的回复（quit停止）：\t")
        response = response.strip()
        while not response:
            print("回复不能为空，请重新输入：")
            response = input("请输入你（顾客）的回复（quit停止）：\t")
            response = response.strip()
        self.messages.append({"role": "assistant", "content": response})
        self.detail_messages.append([self.messages[-1]])
        if response == 'quit':
            response = '###STOP###'
        return response