import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from create_file import Python_File

file = Python_File("")


def create_file() -> None:
    file.create_file()


if __name__ == "__main__":
    create_file()
