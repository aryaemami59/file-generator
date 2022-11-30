from eslint.create_eslint import create_eslint
from eslint.eslint_react_ts import eslint_react_ts, eslintignore_react


if __name__ == "__main__":
    create_eslint(eslint_react_ts, eslintignore_react)
