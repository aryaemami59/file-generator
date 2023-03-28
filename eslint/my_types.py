from typing import Any, Dict, List, Literal, TypedDict


class ENV(TypedDict, total=False):
    browser: bool
    es2022: bool


class ECMAFEATURES(TypedDict, total=False):
    globalReturn: bool
    impliedStrict: bool
    jsx: bool
    experimentalObjectRestSpread: bool


class PARSEROPTIONS(TypedDict, total=False):
    ecmaVersion: Literal[
        3,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        2015,
        2016,
        2017,
        2018,
        2019,
        2020,
        2021,
        2022,
        "latest",
    ]
    sourceType: Literal["script", "module"]
    ecmaFeatures: ECMAFEATURES
    project: List[str]
    tsconfigRootDir: str


Severity = Literal[0, 1, 2]
StringSeverity = Literal["off", "warn", "error"]
RuleLevel = Severity | StringSeverity
RuleEntry = RuleLevel | List[RuleLevel | Any]
Rules = Dict[str, RuleEntry]


class ESLINT_TYPE(TypedDict, total=False):
    env: Dict[str, bool]
    extends: List[str]
    globals: Dict[
        str,
        Literal["off", "readonly", "readable", "writable", "writeable"] | bool,
    ]
    ignorePatterns: str | List[str]
    noInlineConfig: bool
    overrides: List[str]
    parser: Literal["@typescript-eslint/parser"]
    parserOptions: PARSEROPTIONS
    plugins: List[str]
    processor: str
    reportUnusedDisableDirectives: bool
    root: bool
    settings: Dict[str, Any]
    rules: Rules
