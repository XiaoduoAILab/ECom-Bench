from openai import OpenAI
import time

class Doubao1_5ModelClient:
    def __init__(self, api_key, base_url, endpoint_id, console=None):
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.endpoint_id = endpoint_id
        self.console = console

    def create_response(self, messages, tools=None):
        self.console.log("Creating response using Doubao 1.5 model.")
        start_time = time.time()

        if tools:
            completion = self.client.chat.completions.create(
                model=self.endpoint_id,
                messages=messages,
                temperature=0.0,
                tools=tools
            )
        else:
            completion = self.client.chat.completions.create(
                model=self.endpoint_id,
                messages=messages,
                temperature=0.0,
            )

        end_time = time.time()
        self.console.log(f"API response time: {end_time - start_time:.2f} seconds")
        return completion.choices[0].message
