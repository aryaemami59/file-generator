from create_folder import create_folder


react_dirs = ["components", "contexts", "data", "hooks", "types", "utils"]


def create_folder_react_ts() -> None:
    paths = list(map(lambda dir: f"src/{dir}", react_dirs))
    create_folder(paths)


if __name__ == "__main__":
    create_folder_react_ts()
