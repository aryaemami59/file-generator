import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from write_to_all_files import write_to_all_files
import json
from typing import Any


def create_eslint(eslint: dict[str, Any], ignore: str) -> None:
    f = open(f".eslintrc.json", "w")
    json.dump(eslint, f, indent=2, sort_keys=True)
    f.close()
    write_to_all_files([(".eslintignore", ignore)])
