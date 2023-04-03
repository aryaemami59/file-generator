import json
from my_types import _ESLINT_TYPE


def add_redux_eslint() -> None:
    with open(".eslintrc.json", "r") as file:
        data: _ESLINT_TYPE = json.load(file)
    data["extends"].insert(
        data["extends"].index("plugin:react-perf/all"),
        "plugin:react-redux/all",
    )
    data["plugins"].insert(
        data["plugins"].index("jsx-a11y"),
        "react-redux",
    )
    with open(".eslintrc.json", "w") as file:
        json.dump(data, file, indent=2, sort_keys=True)


if __name__ == "__main__":
    add_redux_eslint()
