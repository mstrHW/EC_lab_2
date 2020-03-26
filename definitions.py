import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'data')


def make_dirs(path):
    if not os.path.exists(path):
        os.makedirs(path)
