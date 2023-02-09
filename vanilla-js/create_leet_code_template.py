import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from write_to_all_files import write_to_all_files


def create_leet_code_template(file_name: str) -> None:
    my_js_file = (
        f"{file_name}.js",
        """// Description:


// Challenge:


// Alternate method:


// testing:


""",
    )

    write_to_all_files([my_js_file])


if __name__ == "__main__":
    create_leet_code_template(sys.argv[1])
