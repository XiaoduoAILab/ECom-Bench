from openai import AzureOpenAI


class AzureOpenAIClient:
    def __init__(self, api_base, api_key, api_version, console = None):
        self.client = AzureOpenAI(
            azure_endpoint=api_base,
            api_key=api_key,
            api_version=api_version,
        )
        self.console = console

    def create_response(self, model, messages, tools=None):
        self.console.log(f"Creating response for model {model} using Azure OpenAI.")
        response = self.client.chat.completions.create(
            temperature=0,
            model=model,
            messages=messages,
            tools=tools
        )
        return response.choices[0].message
