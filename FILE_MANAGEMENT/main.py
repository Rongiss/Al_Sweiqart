import shutil
from pathlib import Path


def test():
    shutil.copy(r'new.txt', Path.cwd() / r'new')
    ####


if __name__ == '__main__':
    test()
