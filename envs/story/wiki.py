import os

FOLDER_PATH = os.path.dirname(__file__)

with open(os.path.join(FOLDER_PATH, "wiki.md"), "r", encoding="utf-8") as f:
    WIKI = f.read()