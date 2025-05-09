from utils import LLM

class Agent(LLM):
    def __init__(self, agent_model:str, verbose=False, mcp_tools= []):
        super().__init__(model_name=agent_model, verbose=verbose, mcp_tools=mcp_tools)
        self.agent_model = super()._initiate_agent()
        self.detail_messages = []
    
    
    def load_system_prompt(self, system_prompt):
        self.messages.append({"role": "system", "content": system_prompt})
    
    
    async def call(self, message:str) -> str:
        self.messages.append({"role": "user", "content": message})
        responses = await self.agent_model.ainvoke(
            {
                "messages": self.messages
            }
        )
        self.detail_messages.append(responses["messages"])
        self.messages.append({"role": "assistant", "content": responses["messages"][-1].content})
        # print(self.detail_messages)
        return responses["messages"][-1].content