import requests
import re

class ChatCompletionMessage:
    def __init__(self, content, role='assistant', refusal=None, audio=None, function_call=None, tool_calls=None):
        self.content = content
        self.role = role
        self.refusal = refusal
        self.audio = audio
        self.function_call = function_call
        self.tool_calls = tool_calls
    
    def __str__(self):
        return f"ChatCompletionMessage(content='{self.content}', refusal={self.refusal}, role='{self.role}', audio={self.audio}, function_call={self.function_call}, tool_calls={self.tool_calls})"

    def model_dump(self):
        return {
            "role": self.role,
            "content": self.content,
            "refusal": self.refusal,
            "audio": self.audio,
            "function_call": self.function_call,
            "tool_calls": self.tool_calls
        }
        

class MultimodalModelClient:
    def __init__(self, console=None):
        self.console = console
        self.url_pattern = r'https?://[^\s<>"]+?(?:jpg|jpeg|gif|png|webp)'
        

    def create_response(self, messages, model, tools=None, temperature=0.0, top_p=0.2, max_tokens=128, presence_penalty=1.0, frequency_penalty=1.0, repetition_penalty=1.2):
        parsed_messages = self._prepare_messages(messages)
        model_type = self._get_model_type(model)

        url = " "
        headers = {
            "Content-Type": " ",
            "XdHeader-Auth": " "
        }
        data = {
            "type": model_type,
            "temperature": temperature,
            "generation_config": {
                "temerature": temperature,
                "top_p": top_p,
                "max_tokens": max_tokens,
                "presence_penalty": presence_penalty,
                "frequency_penalty": frequency_penalty,
                "repetition_penalty": repetition_penalty
            },
            "generic_msgs": parsed_messages
        }

        self.console.log("Sending request to multimodal model.")
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            try:
                multimodal_reply = result.get('data', {}).get('answer', '')
                response_obj = ChatCompletionMessage(
                    content=multimodal_reply,
                    role='assistant',
                    refusal=None,
                    audio=None,
                    function_call=None,
                    tool_calls=None
                )
                return response_obj
            except Exception as e:
                self.console.log(f"Error parsing response: {e}")
                return ChatCompletionMessage(
                    content="抱歉，处理请求时出现错误。",
                    role='assistant'
                )
        else:
            self.console.log(f"Request failed with status code: {response.status_code}")
            return ChatCompletionMessage(
                content=f"请求失败 (状态码: {response.status_code})",
                role='assistant'
            )
            
    def _prepare_messages(self, messages):
        parsed_messages = []
        # This method can be implemented to process messages before sending
        for message in messages:
            if not isinstance(message.get('content'), str):
                continue
            text = message.get("content", "")
            role = message.get("role", "user")
            image_match = re.findall(self.url_pattern, text)
            if image_match:
                for url in image_match:
                    text = text.replace(url, '[IMAGE_URL]')
                text = text.strip()
                if role == "user":
                    parsed_messages.append({
                        "role": role,
                        "list_contents": [
                            {
                                "type": "text",
                                "text": text
                            },
                            {
                                "type": "image_url",
                                "image_url": image_match[0]
                                }
                            ]
                    })
                else:
                    parsed_messages.append({
                        "role": role,
                        "content": text
                    })
            else:
                if role == "user":
                    parsed_messages.append({
                        "role": role,
                        "list_contents": [
                            {
                                "type": "text",
                                "text": text
                            }
                        ]
                    })
                else:
                    parsed_messages.append({
                        "role": role,
                        "content": text
                    })
        return parsed_messages

    def _get_model_type(self, model):
        model_to_type = {
            "doubao-pro": "doubao-pro-vision",
            "qwenvlmax": "qwen-vl-max-0809",
            "gpt4omini": "azure_4o_mini",
            "kimi-8k": "moonshot-v1-8k-vision-preview",
            "kimi-32k": "moonshot-v1-32k-vision-preview",
            "kimi-128k": "moonshot-v1-128k-vision-preview"
        }
        return model_to_type.get(model, "qwenvlmax")
