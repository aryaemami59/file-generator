
from create_folder import create_folder
from create_folder_react_ts import react_dirs
# from clean_rn_app import clean_rn_app

# from write_to_file import write_to_all_files


rn_dirs = react_dirs + ["screens", "styles"]


def create_folder_react_native_ts() -> None:
    create_folder(["src"])
    paths = list(map(lambda dir: f"src/{dir}", rn_dirs))
    create_folder(paths)
    # for f in os.listdir("assets"):
    #     os.remove(os.path.join("assets", f))
    # write_to_all_files([("App.tsx", clean_rn_app)])


# if __name__ == "__main__":
#     create_folder_react_native_ts()
