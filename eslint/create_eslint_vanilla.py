import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from create_eslint import create_eslint
from eslint_vanilla import ESLINT_VANILLA, eslintignore


if __name__ == "__main__":
    create_eslint(ESLINT_VANILLA, eslintignore)
