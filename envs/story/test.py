import sys
import os
import json
sys.path.append('/Users/utopia/Documents/晓多/Ebench')
from agent import OFFLINE_SERVER_DIR, OFFLINE_CACHE_DIR, ActionTools

def _load_data(base_dir):
    data = {}
    files = os.listdir(base_dir)
    json_files = [f for f in files if f.endswith('.json')]
    if len(json_files) == 0:
        return data
    else:
        for json_file in json_files:
            file_path = os.path.join(base_dir, json_file)
            file_name = os.path.splitext(json_file)[0]
            with open(file_path, 'r',encoding='utf-8') as f:
                data[file_name] = json.load(f)
    return data
data = _load_data('/Users/utopia/Documents/晓多/Ebench/envs/story/data')
arguments = {
    'function_name':'get_logistics_info',
    'data': data,
    "platform": "jd",
    "shop_id": "5de650c946e7c3001814990f",
    "order_id": "314475833175",
    "user_id": "cnjd林韵佩"
}
action_tools = ActionTools()
data, result = action_tools.call_function(**arguments)
print(result)

