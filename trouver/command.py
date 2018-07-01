import sys, getopt
from .scanner import scan_path
from .config import get_config, save_config
from elasticsearch_dsl import connections
import os
from .web import make_app
from waitress import serve

connections.configure(
    default={
        'hosts': 'localhost'
    }
)


def main():
    pass


def scanner_main():
    OPTIONS = "m:"
    args = dict(get_args(OPTIONS, []))
    mount = os.path.abspath(args['-m'])
    if os.path.exists(mount):
        scan_path(mount)
        config = get_config()
        mounts = config.get('mounts', [])

        if mount not in mounts:
            mounts.append(mount)
            config['mounts'] = mounts
            save_config(config)



def web_main():
    OPTIONS = "p:i:"
    args = dict(get_args(OPTIONS, []))
    port = args.get('-p', 6543)
    interface = args.get('-i', 'localhost')
    serve(make_app({}), host=interface, port=port)

def get_args(options, long_options):
    argv = sys.argv[1:]
    return getopt.getopt(argv, options, long_options)[0]
