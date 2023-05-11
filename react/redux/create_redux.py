import os
from redux_files import get_redux_files
from create_folder import create_folder


def create_redux() -> None:
    os.path.isfile("index.tsx")
    # print(os.path.isfile("src/main.tsx"))
    create_folder(["src/redux", "src/types"])
    for f in get_redux_files():
        f.create_file()


if __name__ == "__main__":
    create_redux()
