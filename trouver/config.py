import os
import json

home = os.path.expanduser('~/')
config_file_name = ".trouver.config"
config_file = os.path.join(home, config_file_name)

def get_config():
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return json.loads(f.read())


def save_config(config):
    with open(config_file, 'wb') as f:
        f.write(json.dumps(config))
