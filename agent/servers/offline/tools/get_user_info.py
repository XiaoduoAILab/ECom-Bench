from .utils import get_user
import json

def get_user_info(data, user_id: str):
    user_info = get_user(data, user_id)
    if not user_info:
        return data, f"没有查到用户{user_id}的信息"
    return data, json.dumps(user_info, ensure_ascii=False)