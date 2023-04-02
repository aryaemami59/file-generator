import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from empty_script_js import empty_script_js
from create_file import (
    Styles_CSS_File,
    Index_HTML_File,
)

files = (
    Index_HTML_File(""),
    Styles_CSS_File(""),
    empty_script_js,
)


def create_empty_files() -> None:
    for v in files:
        v.create_file()


if __name__ == "__main__":
    create_empty_files()
