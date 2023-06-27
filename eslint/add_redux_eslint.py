import json
from my_types.my_types import ESLINT_TYPE


def add_redux_eslint() -> None:
    with open(".eslintrc.json", "r") as file:
        data: ESLINT_TYPE = json.load(file)
    if "extends" in data:
        data["extends"].insert(
            data["extends"].index("plugin:react-perf/all"),
            "plugin:react-redux/all",
        )
    if "plugins" in data:
        data["plugins"].insert(
            data["plugins"].index("jsx-a11y"),
            "react-redux",
        )
    with open(".eslintrc.json", "w") as file:
        json.dump(data, file, indent=2, sort_keys=True)


if __name__ == "__main__":
    add_redux_eslint()
