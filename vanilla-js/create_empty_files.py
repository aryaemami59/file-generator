import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from empty_script_js import empty_script_js
from create_file import Empty_File_Current_Dir

files = (
    Empty_File_Current_Dir("index", "html"),
    Empty_File_Current_Dir("styles", "css"),
    empty_script_js,
)


def create_empty_files() -> None:
    for v in files:
        v.create_file()


if __name__ == "__main__":
    create_empty_files()
