import json
from typing import Any


def create_eslint(eslint: dict[str, Any], ignore: str) -> None:
    f = open(f".eslintrc.json", "w")
    json.dump(eslint, f, indent=2, sort_keys=True)
    f.close()
    r = open(f".eslintignore", "w")
    r.write(ignore)
    r.close()
