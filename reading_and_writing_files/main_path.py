# import pathlib

from pathlib import Path
import os


def main():
    for i in range(3):
        print(Path.cwd().parents[i])
    print(os.listdir(Path.cwd()))
    print(list(Path.cwd().glob(r'*.py')))


if __name__ == '__main__':
    main()
