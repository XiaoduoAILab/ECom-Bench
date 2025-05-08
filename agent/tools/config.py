import yaml
import os

_config = None
def get_config():
    global _config
    if _config is None:    
        base_dir = os.path.dirname(__file__)
        with open(os.path.join(base_dir, "config.yaml")):
            _config = yaml.load(open(os.path.join(base_dir,"config.yaml")), Loader=yaml.FullLoader)
    return _config