import os
import yaml
from typing import Dict, Any

# 全局配置对象
_config = None

def get_config() -> Dict[str, Any]:
    """
    获取配置信息，使用单例模式避免重复加载
    """
    global _config
    if _config is None:
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.yaml")) as f:
            _config = yaml.load(f, Loader=yaml.FullLoader)
        
        # 确保缓存目录存在
        cache_dir = _config["data"]["directory"]
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
            
    return _config