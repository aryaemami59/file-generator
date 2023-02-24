import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from create_custom_hooks import create_custom_hooks
from clean_rn_app import clean_rn_app
from create_folder_react_native_ts import create_folder_react_native_ts
from write_to_all_files import write_to_all_files

# from custom_hooks import useCountRender, useDependencyChangeLogger, useMounted
from create_settings import create_settings
from missingTypes import missingTypes
from settings import settings
from utility_functions import utility_functions
from custom_hooks import custom_hooks

rn_files = utility_functions + custom_hooks


def clean_expo() -> None:
    for v in rn_files:
        v.create_file()
    create_folder_react_native_ts()
    create_settings()
    # create_custom_hooks([useCountRender, useDependencyChangeLogger, useMounted])
    write_to_all_files([clean_rn_app, settings])


if __name__ == "__main__":
    clean_expo()
