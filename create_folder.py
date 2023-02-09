from pathlib import Path


def create_folder(new_paths: list[str]) -> None:
    for path in new_paths:
        Path(path).mkdir(parents=True, exist_ok=True)
