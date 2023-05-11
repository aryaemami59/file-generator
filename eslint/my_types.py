import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from typing import (
    Any,
    Dict,
    List,
    Literal,
    TypedDict,
    NotRequired,
    Tuple,
    Union,
)


Watch_File_Kind = Literal[
    "FixedPollingInterval",
    "PriorityPollingInterval",
    "DynamicPriorityPolling",
    "FixedChunkSizePolling",
    "UseFsEvents",
    "UseFsEventsOnParentDirectory",
]

Watch_Directory_Kind = Literal[
    "UseFsEvents",
    "FixedPollingInterval",
    "DynamicPriorityPolling",
    "FixedChunkSizePolling",
]

Polling_Watch_Kind = Literal[
    "FixedInterval",
    "PriorityInterval",
    "DynamicPriority",
    "FixedChunkSize",
]

Severity = Literal[0, 1, 2]
StringSeverity = Literal["off", "warn", "error"]
RuleLevel = Severity | StringSeverity
A = Tuple[RuleLevel]
B = Tuple[RuleLevel, Any]
# RuleEntry = Union[Tuple[RuleLevel, Any], Tuple[RuleLevel]]
RuleEntry = (
    Tuple[RuleLevel, ...]
    | Tuple[RuleLevel]
    # | Tuple[RuleLevel, Any]
    # | Tuple[RuleLevel, Dict[str, Any]]
)


# RuleEntry = RuleLevel | List[RuleLevel | Any]
Default_Rules = Literal[
    "accessor-pairs",
    "array-bracket-newline",
    "array-bracket-spacing",
    "array-callback-return",
    "array-element-newline",
    "arrow-body-style",
    "arrow-parens",
    "arrow-spacing",
    "block-scoped-var",
    "block-spacing",
    "brace-style",
    "camelcase",
    "capitalized-comments",
    "class-methods-use-this",
    "comma-dangle",
    "comma-spacing",
    "comma-style",
    "complexity",
    "computed-property-spacing",
    "consistent-return",
    "consistent-this",
    "constructor-super",
    "curly",
    "default-case",
    "default-case-last",
    "default-param-last",
    "dot-location",
    "dot-notation",
    "eol-last",
    "eqeqeq",
    "for-direction",
    "func-call-spacing",
    "func-name-matching",
    "func-names",
    "func-style",
    "function-call-argument-newline",
    "function-paren-newline",
    "generator-star-spacing",
    "getter-return",
    "grouped-accessor-pairs",
    "guard-for-in",
    "id-denylist",
    "id-length",
    "id-match",
    "implicit-arrow-linebreak",
    "indent",
    "init-declarations",
    "jsx-quotes",
    "key-spacing",
    "keyword-spacing",
    "line-comment-position",
    "linebreak-style",
    "lines-around-comment",
    "lines-between-class-members",
    "logical-assignment-operators",
    "max-classes-per-file",
    "max-depth",
    "max-len",
    "max-lines",
    "max-lines-per-function",
    "max-nested-callbacks",
    "max-params",
    "max-statements",
    "max-statements-per-line",
    "multiline-comment-style",
    "multiline-ternary",
    "new-cap",
    "new-parens",
    "newline-per-chained-call",
    "no-alert",
    "no-array-constructor",
    "no-async-promise-executor",
    "no-await-in-loop",
    "no-bitwise",
    "no-caller",
    "no-case-declarations",
    "no-class-assign",
    "no-compare-neg-zero",
    "no-cond-assign",
    "no-confusing-arrow",
    "no-console",
    "no-const-assign",
    "no-constant-binary-expression",
    "no-constant-condition",
    "no-constructor-return",
    "no-continue",
    "no-control-regex",
    "no-debugger",
    "no-delete-var",
    "no-div-regex",
    "no-dupe-args",
    "no-dupe-class-members",
    "no-dupe-else-if",
    "no-dupe-keys",
    "no-duplicate-case",
    "no-duplicate-imports",
    "no-else-return",
    "no-empty",
    "no-empty-character-class",
    "no-empty-function",
    "no-empty-pattern",
    "no-empty-static-block",
    "no-eq-null",
    "no-eval",
    "no-ex-assign",
    "no-extend-native",
    "no-extra-bind",
    "no-extra-boolean-cast",
    "no-extra-label",
    "no-extra-parens",
    "no-extra-semi",
    "no-fallthrough",
    "no-floating-decimal",
    "no-func-assign",
    "no-global-assign",
    "no-implicit-coercion",
    "no-implicit-globals",
    "no-implied-eval",
    "no-import-assign",
    "no-inline-comments",
    "no-inner-declarations",
    "no-invalid-regexp",
    "no-invalid-this",
    "no-irregular-whitespace",
    "no-iterator",
    "no-label-var",
    "no-labels",
    "no-lone-blocks",
    "no-lonely-if",
    "no-loop-func",
    "no-loss-of-precision",
    "no-magic-numbers",
    "no-misleading-character-class",
    "no-mixed-operators",
    "no-mixed-spaces-and-tabs",
    "no-multi-assign",
    "no-multi-spaces",
    "no-multi-str",
    "no-multiple-empty-lines",
    "no-negated-condition",
    "no-nested-ternary",
    "no-new",
    "no-new-func",
    "no-new-native-nonconstructor",
    "no-new-object",
    "no-new-symbol",
    "no-new-wrappers",
    "no-nonoctal-decimal-escape",
    "no-obj-calls",
    "no-octal",
    "no-octal-escape",
    "no-param-reassign",
    "no-plusplus",
    "no-promise-executor-return",
    "no-proto",
    "no-prototype-builtins",
    "no-redeclare",
    "no-regex-spaces",
    "no-restricted-exports",
    "no-restricted-globals",
    "no-restricted-imports",
    "no-restricted-properties",
    "no-restricted-syntax",
    "no-return-assign",
    "no-return-await",
    "no-script-url",
    "no-self-assign",
    "no-self-compare",
    "no-sequences",
    "no-setter-return",
    "no-shadow",
    "no-shadow-restricted-names",
    "no-sparse-arrays",
    "no-tabs",
    "no-template-curly-in-string",
    "no-ternary",
    "no-this-before-super",
    "no-throw-literal",
    "no-trailing-spaces",
    "no-undef",
    "no-undef-init",
    "no-undefined",
    "no-underscore-dangle",
    "no-unexpected-multiline",
    "no-unmodified-loop-condition",
    "no-unneeded-ternary",
    "no-unreachable",
    "no-unreachable-loop",
    "no-unsafe-finally",
    "no-unsafe-negation",
    "no-unsafe-optional-chaining",
    "no-unused-expressions",
    "no-unused-labels",
    "no-unused-private-class-members",
    "no-unused-vars",
    "no-use-before-define",
    "no-useless-backreference",
    "no-useless-call",
    "no-useless-catch",
    "no-useless-computed-key",
    "no-useless-concat",
    "no-useless-constructor",
    "no-useless-escape",
    "no-useless-rename",
    "no-useless-return",
    "no-var",
    "no-void",
    "no-warning-comments",
    "no-whitespace-before-property",
    "no-with",
    "nonblock-statement-body-position",
    "object-curly-newline",
    "object-curly-spacing",
    "object-property-newline",
    "object-shorthand",
    "one-var",
    "one-var-declaration-per-line",
    "operator-assignment",
    "operator-linebreak",
    "padded-blocks",
    "padding-line-between-statements",
    "prefer-arrow-callback",
    "prefer-const",
    "prefer-destructuring",
    "prefer-exponentiation-operator",
    "prefer-named-capture-group",
    "prefer-numeric-literals",
    "prefer-object-has-own",
    "prefer-object-spread",
    "prefer-promise-reject-errors",
    "prefer-regex-literals",
    "prefer-rest-params",
    "prefer-spread",
    "prefer-template",
    "quote-props",
    "quotes",
    "radix",
    "require-atomic-updates",
    "require-await",
    "require-unicode-regexp",
    "require-yield",
    "rest-spread-spacing",
    "semi",
    "semi-spacing",
    "semi-style",
    "sort-imports",
    "sort-keys",
    "sort-vars",
    "space-before-blocks",
    "space-before-function-paren",
    "space-in-parens",
    "space-infix-ops",
    "space-unary-ops",
    "spaced-comment",
    "strict",
    "switch-colon-spacing",
    "symbol-description",
    "template-curly-spacing",
    "template-tag-spacing",
    "unicode-bom",
    "use-isnan",
    "valid-typeof",
    "vars-on-top",
    "wrap-iife",
    "wrap-regex",
    "yield-star-spacing",
    "yoda",
]
Rules = Dict[str, RuleEntry]


Ecma_Version = Literal[
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

Source_Type = Literal["script", "module"]

Globals = Dict[
    str,
    Literal["off", "readonly", "readable", "writable", "writeable"] | bool,
]


class ENV(TypedDict, total=False):
    browser: bool
    es2022: bool


class ECMA_FEATURES(TypedDict, total=False):
    experimentalObjectRestSpread: bool
    globalReturn: bool
    impliedStrict: bool
    jsx: bool


class Config_Override(TypedDict):
    excludedFiles: NotRequired[str | List[str] | None]
    files: str | List[str]


class Parser_Options(TypedDict, total=False):
    ecmaFeatures: ECMA_FEATURES
    ecmaVersion: Ecma_Version
    project: List[str]
    sourceType: Source_Type
    tsconfigRootDir: str


class _ESLINT_TYPE(TypedDict, total=False):
    env: Dict[str, bool]
    extends: List[str]
    globals: Globals
    ignorePatterns: str | List[str]
    noInlineConfig: bool
    overrides: List[str]
    parser: Literal["@typescript-eslint/parser"]
    parserOptions: Parser_Options
    plugins: List[str]
    processor: str
    reportUnusedDisableDirectives: bool
    root: bool
    rules: Rules
    settings: Dict[str, Any]


class ESLINT_TYPE(_ESLINT_TYPE, total=True):
    pass
    # env: Dict[str, bool]
    # extends: List[str]
    # globals: Globals
    # ignorePatterns: str | List[str]
    # noInlineConfig: bool
    # overrides: List[str]
    # parser: Literal["@typescript-eslint/parser"]
    # parserOptions: Parser_Options
    # plugins: List[str]
    # processor: str
    # reportUnusedDisableDirectives: bool
    # root: bool
    # rules: Rules
    # settings: Dict[str, Any]


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

New_Line_Kind = Literal["crlf", "lf"]


class _COMPILER_OPTIONS(TypedDict):
    allowArbitraryExtensions: bool
    allowImportingTsExtensions: bool
    allowJs: bool
    allowSyntheticDefaultImports: bool
    allowUmdGlobalAccess: bool
    allowUnreachableCode: bool
    allowUnusedLabels: bool
    alwaysStrict: bool
    assumeChangesOnlyAffectDirectDependencies: bool
    baseUrl: str
    charset: str
    checkJs: bool
    composite: bool
    customConditions: List[str]
    declaration: bool
    declarationDir: str
    declarationMap: bool
    emitBOM: bool
    emitDeclarationOnly: bool
    emitDecoratorMetadata: bool
    esModuleInterop: bool
    exactOptionalPropertyTypes: bool
    experimentalDecorators: bool
    forceConsistentCasingInFileNames: bool
    ignoreDeprecations: str
    importHelpers: bool
    importsNotUsedAsValues: ImportsNotUsedAsValues
    incremental: bool
    inlineSourceMap: bool
    inlineSources: bool
    isolatedModules: bool
    jsx: Jsx_Emit
    jsxFactory: str
    jsxFragmentFactory: str
    jsxImportSource: str
    keyofStringsOnly: bool
    lib: List[str]
    locale: str
    mapRoot: str
    maxNodeModuleJsDepth: float
    module: Module_Kind
    moduleDetection: Module_Detection_Kind
    moduleResolution: Module_Resolution_Kind
    moduleSuffixes: List[str]
    newLine: New_Line_Kind
    noEmit: bool
    noEmitHelpers: bool
    noEmitOnError: bool
    noErrorTruncation: bool
    noFallthroughCasesInSwitch: bool
    noImplicitAny: bool
    noImplicitOverride: bool
    noImplicitReturns: bool
    noImplicitThis: bool
    noImplicitUseStrict: bool
    noLib: bool
    noResolve: bool
    noStrictGenericChecks: bool
    noUncheckedIndexedAccess: bool
    noUnusedLocals: bool
    noUnusedParameters: bool
    out: str
    outDir: str
    outFile: str
    preserveConstEnums: bool
    preserveSymlinks: bool
    preserveValueImports: bool
    project: str
    reactNamespace: str
    removeComments: bool
    resolveJsonModule: bool
    resolvePackageJsonExports: bool
    resolvePackageJsonImports: bool
    rootDir: str
    rootDirs: List[str]
    skipDefaultLibCheck: bool
    skipLibCheck: bool
    sourceMap: bool
    sourceRoot: str
    strict: bool
    strictBindCallApply: bool
    strictFunctionTypes: bool
    strictNullChecks: bool
    strictPropertyInitialization: bool
    stripInternal: bool
    suppressExcessPropertyErrors: bool
    suppressImplicitAnyIndexErrors: bool
    target: Script_Target
    traceResolution: bool
    tsBuildInfoFile: str
    types: List[str]
    typeRoots: List[str]
    useDefineForClassFields: bool
    useUnknownInCatchVariables: bool
    verbatimModuleSyntax: bool


class COMPILER_OPTIONS(_COMPILER_OPTIONS, total=False):
    allowArbitraryExtensions: bool
    allowImportingTsExtensions: bool
    allowJs: bool
    allowSyntheticDefaultImports: bool
    allowUmdGlobalAccess: bool
    allowUnreachableCode: bool
    allowUnusedLabels: bool
    alwaysStrict: bool
    assumeChangesOnlyAffectDirectDependencies: bool
    baseUrl: str
    charset: str
    checkJs: bool
    composite: bool
    customConditions: List[str]
    declaration: bool
    declarationDir: str
    declarationMap: bool
    emitBOM: bool
    emitDeclarationOnly: bool
    emitDecoratorMetadata: bool
    esModuleInterop: bool
    exactOptionalPropertyTypes: bool
    experimentalDecorators: bool
    forceConsistentCasingInFileNames: bool
    ignoreDeprecations: str
    importHelpers: bool
    importsNotUsedAsValues: ImportsNotUsedAsValues
    incremental: bool
    inlineSourceMap: bool
    inlineSources: bool
    isolatedModules: bool
    jsx: Jsx_Emit
    jsxFactory: str
    jsxFragmentFactory: str
    jsxImportSource: str
    keyofStringsOnly: bool
    lib: List[str]
    locale: str
    mapRoot: str
    maxNodeModuleJsDepth: float
    module: Module_Kind
    moduleDetection: Module_Detection_Kind
    moduleResolution: Module_Resolution_Kind
    moduleSuffixes: List[str]
    newLine: New_Line_Kind
    noEmit: bool
    noEmitHelpers: bool
    noEmitOnError: bool
    noErrorTruncation: bool
    noFallthroughCasesInSwitch: bool
    noImplicitAny: bool
    noImplicitOverride: bool
    noImplicitReturns: bool
    noImplicitThis: bool
    noImplicitUseStrict: bool
    noLib: bool
    noResolve: bool
    noStrictGenericChecks: bool
    noUncheckedIndexedAccess: bool
    noUnusedLocals: bool
    noUnusedParameters: bool
    out: str
    outDir: str
    outFile: str
    preserveConstEnums: bool
    preserveSymlinks: bool
    preserveValueImports: bool
    project: str
    reactNamespace: str
    removeComments: bool
    resolveJsonModule: bool
    resolvePackageJsonExports: bool
    resolvePackageJsonImports: bool
    rootDir: str
    rootDirs: List[str]
    skipDefaultLibCheck: bool
    skipLibCheck: bool
    sourceMap: bool
    sourceRoot: str
    strict: bool
    strictBindCallApply: bool
    strictFunctionTypes: bool
    strictNullChecks: bool
    strictPropertyInitialization: bool
    stripInternal: bool
    suppressExcessPropertyErrors: bool
    suppressImplicitAnyIndexErrors: bool
    target: Script_Target
    traceResolution: bool
    tsBuildInfoFile: str
    types: List[str]
    typeRoots: List[str]
    useDefineForClassFields: bool
    useUnknownInCatchVariables: bool
    verbatimModuleSyntax: bool


class Build_Options(TypedDict, total=False):
    dry: bool
    force: bool
    verbose: bool
    incremental: bool
    assumeChangesOnlyAffectDirectDependencies: bool
    declaration: bool
    declarationMap: bool
    emitDeclarationOnly: bool
    sourceMap: bool
    inlineSourceMap: bool
    traceResolution: bool


class REFERENCES(TypedDict, total=False):
    path: str


class Type_Acquisition(TypedDict, total=False):
    enable: bool
    include: List[str]
    exclude: List[str]
    disableFilenameBasedTypeAcquisition: bool


class Watch_Options(TypedDict, total=False):
    watchFile: Watch_File_Kind
    watchDirectory: Watch_Directory_Kind
    fallbackPolling: Polling_Watch_Kind
    synchronousWatchDirectory: bool
    excludeDirectories: List[str]
    excludeFiles: List[str]


class TS_CONFIG_TYPE_REQUIRED(TypedDict):
    buildOptions: Build_Options
    compileOnSave: bool
    compilerOptions: COMPILER_OPTIONS
    files: List[str]
    include: List[str]
    exclude: List[str]
    extends: List[str] | str
    references: List[REFERENCES]
    typeAcquisition: Type_Acquisition
    watchOptions: Watch_Options


class TS_CONFIG_TYPE(TS_CONFIG_TYPE_REQUIRED, total=False):
    buildOptions: Build_Options
    compileOnSave: bool
    compilerOptions: COMPILER_OPTIONS
    files: List[str]
    include: List[str]
    exclude: List[str]
    extends: List[str] | str
    references: List[REFERENCES]
    typeAcquisition: Type_Acquisition
    watchOptions: Watch_Options


# qq: B = (
#     2,
#     {
#         "arrowParens": "avoid",
#         "bracketSameLine": True,
#         "endOfLine": "auto",
#         "singleAttributePerLine": True,
#     },
# )

# hh = {"prettier/prettier": qq}

# hh["prettier/prettier"][1]

# aa: Rules = {"prettier/prettier": qq}

# if len(aa["prettier/prettier"]) == 2:
#     aa["prettier/prettier"][1]


# MyTuple = Union[Tuple[int], Tuple[int, str]]

# tuple1: MyTuple = (10,)
# tuple2: MyTuple = (20, "Hello")
