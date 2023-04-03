import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from clean_react_vite_app import clean_react_vite_app
from clean_react_vite_main import clean_react_vite_main
from clean_react_index_html import clean_react_index_html
from write_to_all_files import write_to_all_files
from vite_config import vite_config, react_ts_config
from missingTypes import missingTypes
from create_folder import create_folder
from settings import settings
from utility_functions import utility_functions
from react.custom_hooks import custom_hooks, logger_hooks
from create_settings import create_settings
import os

react_folders = [
    "components",
    "contexts",
    "data",
    "hooks",
    "types",
    "utils",
    "hooks/loggers",
]


react_dirs = list(map(lambda dir: f"src/{dir}", react_folders))
react_files = (
    utility_functions
    + custom_hooks
    + logger_hooks
    + (
        clean_react_index_html,
        clean_react_vite_app,
        clean_react_vite_main,
        vite_config,
        react_ts_config,
        missingTypes,
    )
)


def create_react_vite() -> None:
    create_folder([".vscode"])
    create_settings()
    create_folder(react_dirs)
    for u in react_files:
        u.create_file()
    write_to_all_files(
        [
            ("src/App.css", ""),
            ("README.md", "# New Project"),
            # settings,
        ]
    )
    os.remove("src/index.css")
    os.remove("src/assets/react.svg")
    os.remove("public/vite.svg")


if __name__ == "__main__":
    create_react_vite()
