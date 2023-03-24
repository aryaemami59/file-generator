import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from clean_rn_app import clean_rn_app
from write_to_all_files import write_to_all_files
from settings import settings
from utility_functions import utility_functions
from custom_hooks import custom_hooks, logger_hooks
from create_folder import create_folder
from settings import settings
from react.create_react_vite import react_folders
from missingTypes import missingTypes
from rn_extra_files import rn_extra_files

rn_folders = react_folders + ["screens", "styles"]
rn_dirs = list(map(lambda dir: f"src/{dir}", rn_folders))
rn_files = (
    utility_functions
    + custom_hooks
    + logger_hooks
    + (clean_rn_app, missingTypes)
    + rn_extra_files
)


def create_rn_expo() -> None:
    create_folder([".vscode"])
    create_folder(rn_dirs)
    for v in rn_files:
        v.create_file()
    write_to_all_files([settings, ("README.md", "# New Project")])


if __name__ == "__main__":
    create_rn_expo()
