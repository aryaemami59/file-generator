from typing import (
    TypedDict,
    NotRequired,
    Literal,
    Any,
    Generic,
    TypeVar,
    List,
    Tuple,
    Dict,
)

Severity = Literal[Literal[0], Literal[1], Literal[2]]

StringSeverity = Literal[Literal["off"], Literal["warn"], Literal["error"]]

RuleLevel = Severity | StringSeverity

RuleEntry = RuleLevel | Tuple[RuleLevel, Any]

RulesRecord = Dict[str, RuleEntry]

Rules = TypeVar("Rules")


class HasRules(Generic[Rules], Generic[TypedDict]):
    rules: NotRequired[Rules | None]


ECMAVERSION = Literal[
    Literal[3],
    Literal[5],
    Literal[6],
    Literal[7],
    Literal[8],
    Literal[9],
    Literal[10],
    Literal[11],
    Literal[12],
    Literal[2015],
    Literal[2016],
    Literal[2017],
    Literal[2018],
    Literal[2019],
    Literal[2020],
    Literal[2021],
    Literal[2022],
    Literal["latest"],
]

SOURCETYPE = Literal[Literal["script"], Literal["module"]]


class ECMAFEATURES_0(TypedDict):
    globalReturn: NotRequired[bool | None]
    impliedStrict: NotRequired[bool | None]
    jsx: NotRequired[bool | None]
    experimentalObjectRestSpread: NotRequired[bool | None]


ECMAFEATURES = ECMAFEATURES_0


class ParserOptions_0(TypedDict):
    ecmaVersion: NotRequired[ECMAVERSION | None]
    sourceType: NotRequired[SOURCETYPE | None]
    ecmaFeatures: NotRequired[ECMAFEATURES | None]


ParserOptions = ParserOptions_0

ENV = Dict[str, bool]

G = Literal[
    Literal["off"],
    Literal["readonly"],
    Literal["readable"],
    Literal["writable"],
    Literal["writeable"],
]

GLOBALS = Dict[str, G | bool]

Rules = TypeVar("Rules")


class BaseConfig(HasRules[Rules], Generic[Rules]):
    env: NotRequired[ENV | None]
    extends: NotRequired[str | List[str] | None]
    globals: NotRequired[GLOBALS | None]
    noInlineConfig: NotRequired[bool | None]
    overrides: NotRequired[List[str] | None]
    parser: NotRequired[str | None]
    parserOptions: NotRequired[ParserOptions | None]
    plugins: NotRequired[List[str] | None]
    processor: NotRequired[str | None]
    reportUnusedDisableDirectives: NotRequired[bool | None]
    settings: NotRequired[Dict[str, Any] | None]


Rules = TypeVar("Rules")


class Config(BaseConfig[Rules], Generic[Rules]):
    ignorePatterns: NotRequired[str | List[str] | None]
    root: NotRequired[bool | None]
