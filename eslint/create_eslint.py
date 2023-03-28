import sys
import path
import json


folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from my_types import ESLINT_TYPE

from write_to_all_files import write_to_all_files


def create_eslint(eslint: ESLINT_TYPE, ignore: str) -> None:
    f = open(".eslintrc.json", "w")
    json.dump(eslint, f, indent=2, sort_keys=True)
    f.close()
    write_to_all_files([(".eslintignore", ignore)])
