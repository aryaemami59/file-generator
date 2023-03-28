# import sys
# import path

# folder = path.Path(__file__).abspath()
# sys.path.append(folder.parent.parent)
# from typing import Any, Dict, List, Literal, NotRequired, TypedDict


# class ENV(TypedDict, total=False):
#     browser: bool
#     es2022: bool


# class ECMAFEATURES(TypedDict):
#     globalReturn: NotRequired[bool]
#     impliedStrict: NotRequired[bool]
#     jsx: NotRequired[bool]
#     experimentalObjectRestSpread: NotRequired[bool]


# class PARSEROPTIONS(TypedDict, total=False):
#     ecmaVersion: NotRequired[
#         Literal[
#             3,
#             5,
#             6,
#             7,
#             8,
#             9,
#             10,
#             11,
#             12,
#             2015,
#             2016,
#             2017,
#             2018,
#             2019,
#             2020,
#             2021,
#             2022,
#             "latest",
#         ]
#     ]
#     sourceType: NotRequired[Literal["script", "module"]]
#     ecmaFeatures: NotRequired[ECMAFEATURES]
#     project: List[str]
#     tsconfigRootDir: str


# Severity = Literal[0, 1, 2]
# StringSeverity = Literal["off", "warn", "error"]
# RuleLevel = Severity | StringSeverity
# RuleEntry = RuleLevel | List[RuleLevel | Any]
# Rules = Dict[str, RuleEntry]


# class ESLINT(TypedDict, total=False):
#     env: NotRequired[Dict[str, bool]]
#     extends: NotRequired[List[str]]
#     globals: NotRequired[
#         Dict[
#             str,
#             Literal["off", "readonly", "readable", "writable", "writeable"]
#             | bool,
#         ]
#     ]
#     ignorePatterns: NotRequired[str | List[str]]
#     noInlineConfig: NotRequired[bool]
#     overrides: NotRequired[List[str]]
#     parser: NotRequired[Literal["@typescript-eslint/parser"]]
#     parserOptions: NotRequired[PARSEROPTIONS]
#     plugins: NotRequired[List[str]]
#     processor: NotRequired[str]
#     reportUnusedDisableDirectives: NotRequired[bool]
#     root: NotRequired[bool]
#     settings: NotRequired[Dict[str, Any]]
#     rules: NotRequired[Rules]


from my_types import ESLINT_TYPE


ESLINT_VANILLA: ESLINT_TYPE = {
    "env": {"browser": True, "es2022": True},
    "extends": [
        "eslint:recommended",
        "airbnb-base",
        "plugin:prettier/recommended",
    ],
    "overrides": [],
    "parserOptions": {"ecmaVersion": "latest", "sourceType": "module"},
    "plugins": ["prefer-arrow-functions", "prettier"],
    "root": True,
    "rules": {
        "no-console": [0],
        "no-param-reassign": [2, {"props": False}],
        "prefer-arrow-functions/prefer-arrow-functions": [
            2,
            {
                "classPropertiesAllowed": False,
                "disallowPrototype": True,
                "returnStyle": "unchanged",
                "singleReturnOnly": False,
            },
        ],
        "prettier/prettier": [
            2,
            {
                "arrowParens": "avoid",
                "bracketSameLine": True,
                "endOfLine": "auto",
                "singleAttributePerLine": True,
            },
        ],
    },
}


eslintignore = "node_modules\n.vscode\ntsconfig.json"
