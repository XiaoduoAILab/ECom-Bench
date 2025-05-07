import yaml
import os

def get_config():
    base_dir = os.path.dirname(__file__)
    with open(os.path.join(base_dir, "config.yaml")):
        config = yaml.load(open(os.path.join(base_dir,"config.yaml")), Loader=yaml.FullLoader)
    return config