import os
base_dir = os.path.dirname(__file__)
with open(os.path.join(base_dir, "agent_wiki.md"), "r", encoding="utf-8") as f:
    AGENT_WIKI = f.read()
