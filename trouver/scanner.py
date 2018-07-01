import os


def iter_file_paths(dir_path):
    dir_path_ = os.path.abspath(dir_path)
    for cur_dir, dirs, files in os.walk(dir_path_):
        for f in files:
            yield os.path.join(cur_dir, f)
