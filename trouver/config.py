import os
import json

home = os.path.expanduser('~/')
config_file_name = ".trouver.config"
config_file = os.path.join(home, config_file_name)

def get_config():
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            try:
                return json.loads(f.read())
            except json.JSONDecodeError as e:
                return {}
    else:
        return {}

def save_config(config):
    with open(config_file, 'w') as f:
        f.write(json.dumps(config))
