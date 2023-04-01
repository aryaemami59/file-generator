import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
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


TARGET = Literal[
    "ES3",
    "ES5",
    "ES2015",
    "ES2016",
    "ES2017",
    "ES2018",
    "ES2019",
    "ES2020",
    "ES2021",
    "ES2022",
    "ESNext",
    "JSON",
    "Latest",
]

from enum import Enum


# class ImportsNotUsedAsValues(Enum):
#     Remove = 0
#     Preserve = 1
#     Error = 2


ImportsNotUsedAsValues = Literal["remove", "preserve", "error"]
Script_Target = Literal[
    "ES3",
    "ES5",
    "ES2015",
    "ES2016",
    "ES2017",
    "ES2018",
    "ES2019",
    "ES2020",
    "ES2021",
    "ES2022",
    "ESNext",
]

Module_Kind = Literal[
    "AMD",
    "CommonJS",
    "ES2015",
    "ES2020",
    "ES2022",
    "ES6",
    "ESNext",
    "Node16",
    "NodeNext",
    "None",
    "System",
    "UMD",
]

Module_Resolution_Kind = Literal[
    "bundler",
    "classic",
    "node",
    "node16",
    "nodenext",
]

Jsx_Emit = Literal[
    "preserve",
    "react",
    "react-jsx",
    "react-jsxdev",
    "react-native",
]

Module_Detection_Kind = Literal["legacy", "auto", "force"]


class COMPILER_OPTIONS(TypedDict, total=False):
    allowImportingTsExtensions: bool
    allowJs: bool
    allowArbitraryExtensions: bool
    allowSyntheticDefaultImports: bool
    allowUmdGlobalAccess: bool
    allowUnreachableCode: bool
    allowUnusedLabels: bool
    alwaysStrict: bool
    baseUrl: str
    charset: str
    checkJs: bool
    customConditions: List[str]
    declaration: bool
    declarationMap: bool
    emitDeclarationOnly: bool
    declarationDir: str
    disableSizeLimit: bool
    disableSourceOfProjectReferenceRedirect: bool
    disableSolutionSearching: bool
    disableReferencedProjectLoad: bool
    downlevelIteration: bool
    emitBOM: bool
    emitDecoratorMetadata: bool
    exactOptionalPropertyTypes: bool
    experimentalDecorators: bool
    forceConsistentCasingInFileNames: bool
    ignoreDeprecations: str
    importHelpers: bool
    importsNotUsedAsValues: ImportsNotUsedAsValues
    inlineSourceMap: bool
    inlineSources: bool
    isolatedModules: bool
    jsx: Jsx_Emit
    keyofStringsOnly: bool
    lib: List[str]
    locale: str
    mapRoot: str
    maxNodeModuleJsDepth: int
    module: Module_Kind
    moduleResolution: Module_Resolution_Kind
    moduleSuffixes: List[str]
    moduleDetection: Module_Detection_Kind
    target: Script_Target
    useDefineForClassFields: bool
    allowJs: bool
    skipLibCheck: bool
    esModuleInterop: bool
    allowSyntheticDefaultImports: bool
    strict: bool
    forceConsistentCasingInFileNames: bool
    resolveJsonModule: bool
    isolatedModules: bool
    noEmit: bool
    noUnusedLocals: bool
    noUnusedParameters: bool
    noEmitHelpers: bool
    noEmitOnError: bool
    noErrorTruncation: bool
    noFallthroughCasesInSwitch: bool
    noImplicitAny: bool
    noImplicitReturns: bool
    noImplicitThis: bool
    noStrictGenericChecks: bool
    noUnusedLocals: bool
    noUnusedParameters: bool
    noImplicitUseStrict: bool
    types: List[str]


class REFERENCES(TypedDict, total=False):
    path: str


class TS_CONFIG_TYPE(TypedDict, total=False):
    compilerOptions: COMPILER_OPTIONS
    files: List[str]
    include: List[str]
    exclude: List[str]
    extends: List[str] | str
    references: List[REFERENCES]
