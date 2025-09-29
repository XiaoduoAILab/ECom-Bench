from openai import OpenAI

class DeepseekV3ModelClient:
    def __init__(self, api_key, base_url, endpoint_id, console=None):
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.endpoint_id = endpoint_id
        self.console = console

    def create_response(self, messages, tools=None):
        self.console.log("Creating response using Deepseek V3 model.")
        completion = self.client.chat.completions.create(
            model=self.endpoint_id,
            messages=messages,
            temperature=0.0,
            tools=tools
        )
        return completion.choices[0].message
