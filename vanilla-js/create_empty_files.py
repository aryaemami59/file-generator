import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from write_to_all_files import write_to_all_files
from empty_script_js import empty_script_js


def create_empty_files() -> None:
    write_to_all_files([("index.html", ""), ("styles.css", ""), empty_script_js])


if __name__ == "__main__":
    create_empty_files()
