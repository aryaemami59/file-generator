from react.create_folder import create_folder
from react.create_folder_react_ts import react_dirs

rn_dirs = react_dirs + ["screens", "styles"]


def create_folder_react_native_ts() -> None:
    create_folder(["src"])
    paths = list(map(lambda dir: f"src/{dir}", rn_dirs))
    create_folder(paths)
