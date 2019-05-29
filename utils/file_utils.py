import os


def path_exists(path):
    """路径是否存在，不存在则创建"""
    if not os.path.exists(path):
        print(path, '不存在，即将创建')
        os.makedirs(path)
