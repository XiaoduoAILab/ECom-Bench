from openai import OpenAI
import time

class QwenModelClient:
    def __init__(self, api_key, base_url, console=None):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.console = console

    def create_response(self, messages, tools=None):
        self.console.log("Creating response using Qwen model.")
        start_time = time.time()

        if tools:
            completion = self.client.chat.completions.create(
                model="qwen-max",
                messages=messages,
                tools=tools,
                temperature=0,
            )
        else:
            completion = self.client.chat.completions.create(
                model="qwen-max",
                messages=messages,
                temperature=0,
            )
        
        end_time = time.time()
        self.console.log(f"API response time: {end_time - start_time:.2f} seconds")
        return completion.choices[0].message
