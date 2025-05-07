from utils import LLM
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import List,Tuple, Any
import sys
import json
import traceback

class Task(BaseModel):
    """表示客户与客服交互过程中的单个子任务，用于评估客服对特定客户意图的响应质量"""
    intention: str = Field(description="客户在当前子任务中明确或隐含表达的具体意图或需求")
    service: str = Field(description="客服针对该特定意图所提供的实际回复内容或服务内容")
    reason: str = Field(description="详细分析客服回复是否满足客户意图的具体理由，包括回复的相关性、完整性和有效性")
    result: int = Field(description="客服响应满足度评分：1表示充分满足客户需求，0表示未能满足客户需求")

class RewardResult(BaseModel):
    """对一轮完整客户-客服对话中所有不同客户意图的满足情况进行综合评估"""
    tasks: List[Task] = Field(description="包含本轮对话中识别出的所有不同客户意图及对应的客服响应评估，每个意图只评估一次，不允许重复")

class Reward(LLM):
    def __init__(self, reward_model:str):
        super().__init__(model_name=reward_model)
        self.reward_model = self.llm
        self.parser = PydanticOutputParser(pydantic_object=RewardResult)
    
    def load_system_prompt(self, system_prompt):
        return super().load_system_prompt(system_prompt)
    
    def call(self, rules, history) -> Tuple[float, Any]:
        prompt_template = PromptTemplate(
            template="""假设你是一个评分专家，请你根据以下信息，评估AI客服回复的质量。
# 评分规则：
{rules}

# 顾客提问和客服回复的历史记录：
{history}

输出格式：
{format_instructions}""",
            input_variables=["rules", "history"],
            partial_variables={"format_instructions": self.parser.get_format_instructions()},
        )
        
        # 生成提示
        prompt = prompt_template.format(
            rules = rules,
            history = history
        )
        try:
            # 获取评估结果
            result = self.reward_model.invoke(prompt).content
            parsed_result = self.parser.parse(result)
            return (self.parse_score(parsed_result), json.dumps(parsed_result.model_dump(), ensure_ascii=False, indent=2))
        except Exception as e:
            # 获取错误发生的文件和行号
            exc_type, exc_obj, exc_tb = sys.exc_info()
            filename = exc_tb.tb_frame.f_code.co_filename
            line_no = exc_tb.tb_lineno
            
            # 简洁的错误信息
            error_msg = (
                f"评估出错：{str(e)}\n"
                f"位置：{filename} 第 {line_no} 行\n"
                f"错误类型：{type(e).__name__}"
            )
            
            print(f"Error occurred: {error_msg}")  # 打印到日志
            traceback.print_exc()  # 打印完整堆栈（可选）
            
            return (0.0, result)
    
    def parse_score(self, parsed_result):
        total = sum(task.result for task in parsed_result.tasks)
        return round((total/len(parsed_result.tasks)), 2)
                    
if __name__ == '__main__':
    reward = Reward("deepseek-v3")
    