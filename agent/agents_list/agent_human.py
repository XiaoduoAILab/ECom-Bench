from utils import LLM

class AgentHuman(LLM):
    def __init__(self, agent_model:str, verbose=False, mcp_tools= []):
        super().__init__(model_name=agent_model, verbose=verbose, mcp_tools=mcp_tools)
        self.agent_model = super()._initiate_agent()
        self.detail_messages = []
    
    def load_system_prompt(self, system_prompt):
        self.messages.append({"role": "system", "content": system_prompt})
    
    async def call(self, message:str) -> str:
        self.messages.append({"role": "user", "content": message})
        response = input("请输入你（客服）的回复:\t")
        response = response.strip()
        
        while not response:
            print("回复不能为空，请重新输入!")
            response = input("请输入你（客服）的回复:\t")
            response = response.strip()
            
        self.messages.append({"role": "assistant", "content": response})
        self.detail_messages.append([{"role": "assistant", "content": response}])
        return response