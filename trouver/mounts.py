from .config import load_config, save_config


def save_mounts(mounts):
    config = load_config()
    config['mounts'] = mounts
    save_config(config)


def load_mounts():
    config = load_config()
    return config.get('mounts', [])
