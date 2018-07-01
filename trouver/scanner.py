import os
from .indexer import is_supported_type
from .document import Document

def iter_file_paths(dir_path):
    dir_path_ = os.path.abspath(dir_path)
    for cur_dir, dirs, files in os.walk(dir_path_):
        for f in files:
            yield os.path.join(cur_dir, f)


def scan_path(dir_path):
    for f in [f for f in iter_file_paths(dir_path)]:
        print(f"indexing {f}")
        Document.create_from_file_path(f)
