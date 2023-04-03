# eslint_react_ts = {
#     "env": {"browser": True, "es2022": True},
#     "extends": [
#         "eslint:recommended",
#         "plugin:@typescript-eslint/eslint-recommended",
#         "airbnb",
#         "airbnb-typescript",
#         "airbnb/hooks",
#         "react-app",
#         "plugin:react/recommended",
#         "plugin:react/jsx-runtime",
#         "plugin:jsx-a11y/strict",
#         "plugin:react-redux/all",
#         "plugin:react-perf/all",
#         "plugin:@typescript-eslint/recommended",
#         "plugin:@typescript-eslint/recommended-requiring-type-checking",
#         "plugin:@typescript-eslint/strict",
#         "plugin:prettier/recommended",
#     ],
#     "overrides": [],
#     "parser": "@typescript-eslint/parser",
#     "parserOptions": {
#         "ecmaFeatures": {"jsx": True},
#         "ecmaVersion": "latest",
#         "project": ["./tsconfig.json"],
#         "sourceType": "module",
#         "tsconfigRootDir": "./",
#     },
#     "plugins": [
#         "react",
#         "@typescript-eslint",
#         "prefer-arrow-functions",
#         "react-perf",
#         "prettier",
#         "react-redux",
#         "jsx-a11y",
#     ],
#     "root": True,
#     "rules": {
#         "@typescript-eslint/consistent-type-definitions": [2, "type"],
#         "@typescript-eslint/consistent-type-imports": [2],
#         "@typescript-eslint/naming-convention": [
#             2,
#             {"format": ["PascalCase"], "selector": ["typeLike"]},
#             {
#                 "format": ["PascalCase", "camelCase"],
#                 "selector": ["variable"],
#                 "types": ["function"],
#             },
#             {
#                 "format": ["camelCase", "UPPER_CASE"],
#                 "selector": ["variable"],
#                 "types": ["array", "boolean", "number", "string"],
#             },
#             {
#                 "format": None,
#                 "modifiers": ["requiresQuotes"],
#                 "selector": ["objectLiteralProperty"],
#             },
#             {"format": ["camelCase"], "selector": ["parameter"]},
#         ],
#         "@typescript-eslint/no-floating-promises": [0],
#         "@typescript-eslint/no-throw-literal": [0],
#         "no-console": [0],
#         "no-param-reassign": [2, {"props": False}],
#         "prefer-arrow-functions/prefer-arrow-functions": [2],
#         "prettier/prettier": [
#             2,
#             {
#                 "arrowParens": "avoid",
#                 "bracketSameLine": True,
#                 "parser": "typescript",
#                 "singleAttributePerLine": True,
#             },
#         ],
#         "react/function-component-definition": [
#             2,
#             {
#                 "namedComponents": "arrow-function",
#                 "unnamedComponents": "arrow-function",
#             },
#         ],
#         "react/jsx-props-no-spreading": [0],
#         "react/require-default-props": [0],
#     },
#     "settings": {"react": {"version": "detect"}},
# }

from eslint_vanilla import ESLINT_VANILLA
from my_types import Rules

eslint_react_ts = ESLINT_VANILLA.copy()

eslint_react_ts_rules: Rules = {
    "@typescript-eslint/consistent-type-definitions": (2, "type"),
    "@typescript-eslint/consistent-type-imports": (2,),
    "@typescript-eslint/naming-convention": (
        2,
        {"format": ["PascalCase"], "selector": ["typeLike"]},
        {
            "format": ["PascalCase", "camelCase"],
            "selector": ["variable"],
            "types": ["function"],
        },
        {
            "format": ["camelCase", "UPPER_CASE"],
            "selector": ["variable"],
            "types": ["array", "boolean", "number", "string"],
        },
        {
            "format": None,
            "modifiers": ["requiresQuotes"],
            "selector": ["objectLiteralProperty"],
        },
        {"format": ["camelCase"], "selector": ["parameter"]},
    ),
    "@typescript-eslint/no-floating-promises": (0,),
    "@typescript-eslint/no-throw-literal": (0,),
    "react/function-component-definition": (
        2,
        {
            "namedComponents": "arrow-function",
            "unnamedComponents": "arrow-function",
        },
    ),
    "react/jsx-props-no-spreading": (0,),
    "react/require-default-props": (0,),
}

if "extends" in eslint_react_ts:
    eslint_react_ts["extends"].remove("airbnb-base")
    eslint_react_ts["extends"].remove("plugin:prettier/recommended")
    eslint_react_ts["extends"].extend(
        [
            "plugin:@typescript-eslint/eslint-recommended",
            "airbnb",
            "airbnb-typescript",
            "airbnb/hooks",
            "react-app",
            "plugin:react/recommended",
            "plugin:react/jsx-runtime",
            "plugin:jsx-a11y/strict",
            # "plugin:react-redux/all",
            "plugin:react-perf/all",
            "plugin:@typescript-eslint/recommended",
            "plugin:@typescript-eslint/recommended-requiring-type-checking",
            "plugin:@typescript-eslint/strict",
            "plugin:prettier/recommended",
        ]
    )
eslint_react_ts["parser"] = "@typescript-eslint/parser"
if "parserOptions" in eslint_react_ts:
    eslint_react_ts["parserOptions"].update(
        {
            "ecmaFeatures": {"jsx": True},
            "project": ["./tsconfig.json"],
            "tsconfigRootDir": "./",
        }
    )
if "plugins" in eslint_react_ts:
    eslint_react_ts["plugins"].insert(0, "react")
    eslint_react_ts["plugins"].insert(1, "@typescript-eslint")
    eslint_react_ts["plugins"].insert(3, "react-perf")
    eslint_react_ts["plugins"].extend(["jsx-a11y"])
    # eslint_react_ts["plugins"].extend(["react-redux", "jsx-a11y"])
if "rules" in eslint_react_ts:
    eslint_react_ts["rules"].update(eslint_react_ts_rules)  # type: ignore
    if (
        "prettier/prettier" in eslint_react_ts["rules"]
        and type(eslint_react_ts["rules"]["prettier/prettier"]) is list
        and type(eslint_react_ts["rules"]["prettier/prettier"][1]) is dict
    ):
        eslint_react_ts["rules"]["prettier/prettier"][1][
            "parser"
        ] = "typescript"
eslint_react_ts["settings"] = {"react": {"version": "detect"}}

eslintignore_react = """node_modules
build
dist
.git
.vscode
public
netlify.toml
vite.config.ts
"""
