import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent.parent)

import json
from eslint.my_types import _TS_CONFIG_TYPE


def add_redux_ts_config() -> None:
    with open("tsconfig.json", "r") as file:
        data: _TS_CONFIG_TYPE = json.load(file)
    if "types" in data["compilerOptions"]:
        data["compilerOptions"]["types"].append("node")
    else:
        data["compilerOptions"]["types"] = ["node"]
    with open("tsconfig.json", "w") as file:
        json.dump(data, file, indent=2, sort_keys=True)


if __name__ == "__main__":
    add_redux_ts_config()
