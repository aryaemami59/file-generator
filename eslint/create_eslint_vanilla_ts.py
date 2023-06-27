# import sys
# import path

# folder = path.Path(__file__).abspath()
# sys.path.append(folder.parent.parent)

from create_eslint import create_eslint
from eslint_vanilla_ts import eslint_vanilla_ts

if __name__ == "__main__":
    create_eslint(eslint_vanilla_ts)
