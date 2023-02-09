from create_folder import create_folder
from write_to_all_files import write_to_all_files
from settings import settings


def create_settings() -> None:
    create_folder([".vscode"])
    write_to_all_files([settings])
