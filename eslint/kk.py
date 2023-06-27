import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from dataclasses import dataclass
from typing import Optional, List, Dict, Any, Union
from enum import Enum


@dataclass
class BuildOptionsClass:
    """Have recompiles in projects that use `incremental` and `watch` mode assume that changes
    within a file will only affect files directly depending on it.
    """

    assumeChangesOnlyAffectDirectDependencies: Optional[bool] = None
    """~"""
    dry: Optional[bool] = None
    """Build all projects, including those that appear to be up to date"""
    force: Optional[bool] = None
    """Save .tsbuildinfo files to allow for incremental compilation of projects."""
    incremental: Optional[bool] = None
    """Log paths used during the `moduleResolution` process."""
    traceResolution: Optional[bool] = None
    """Enable verbose logging"""
    verbose: Optional[bool] = None


class FallbackPolling(Enum):
    """Specify the polling strategy to use when the system runs out of or doesn't support native
    file watchers. Requires TypeScript version 3.8 or later.
    """

    dynamicPriority = "dynamicPriority"
    dynamicPriorityPolling = "dynamicPriorityPolling"
    fixedChunkSize = "fixedChunkSize"
    fixedInterval = "fixedInterval"
    fixedPollingInterval = "fixedPollingInterval"
    priorityInterval = "priorityInterval"
    priorityPollingInterval = "priorityPollingInterval"


class ImportsNotUsedAsValues(Enum):
    """Specify emit/checking behavior for imports that are only used for types."""

    error = "error"
    preserve = "preserve"
    remove = "remove"


class Jsx(Enum):
    """Specify what JSX code is generated."""

    preserve = "preserve"
    react = "react"
    reactjsx = "react-jsx"
    reactjsxdev = "react-jsxdev"
    reactnative = "react-native"


@dataclass
class Plugin:
    """Plugin name."""

    name: Optional[str] = None


class WatchDirectory(Enum):
    """Specify the strategy for watching directories under systems that lack recursive
    file-watching functionality. Requires TypeScript version 3.8 or later.
    """

    dynamicPriorityPolling = "dynamicPriorityPolling"
    fixedChunkSizePolling = "fixedChunkSizePolling"
    fixedPollingInterval = "fixedPollingInterval"
    useFsEvents = "useFsEvents"


class WatchFile(Enum):
    """Specify the strategy for watching individual files. Requires TypeScript version 3.8 or
    later.
    """

    dynamicPriorityPolling = "dynamicPriorityPolling"
    fixedChunkSizePolling = "fixedChunkSizePolling"
    fixedPollingInterval = "fixedPollingInterval"
    priorityPollingInterval = "priorityPollingInterval"
    useFsEvents = "useFsEvents"
    useFsEventsOnParentDirectory = "useFsEventsOnParentDirectory"


@dataclass
class TSConfigCompilerOptions:
    """Instructs the TypeScript compiler how to compile .ts files."""

    """Allow JavaScript files to be a part of your program. Use the `checkJS` option to get
    errors from these files.
    """
    allowJs: Optional[bool] = None
    """Allow 'import x from y' when a module doesn't have a default export."""
    allowSyntheticDefaultImports: Optional[bool] = None
    """Allow accessing UMD globals from modules."""
    allowUmdGlobalAccess: Optional[bool] = None
    """Disable error reporting for unreachable code."""
    allowUnreachableCode: Optional[bool] = None
    """Disable error reporting for unused labels."""
    allowUnusedLabels: Optional[bool] = None
    """Ensure 'use strict' is always emitted."""
    alwaysStrict: Optional[bool] = None
    """Have recompiles in '--incremental' and '--watch' assume that changes within a file will
    only affect files directly depending on it. Requires TypeScript version 3.8 or later.
    """
    assumeChangesOnlyAffectDirectDependencies: Optional[bool] = None
    """Specify the base directory to resolve non-relative module names."""
    baseUrl: Optional[str] = None
    """No longer supported. In early versions, manually set the text encoding for reading files."""
    charset: Optional[str] = None
    """Enable error reporting in type-checked JavaScript files."""
    checkJs: Optional[bool] = None
    """Enable constraints that allow a TypeScript project to be used with project references."""
    composite: Optional[bool] = None
    """Generate .d.ts files from my_typescript and JavaScript files in your project."""
    declaration: Optional[bool] = None
    """Specify the output directory for generated declaration files."""
    declarationDir: Optional[str] = None
    """Create sourcemaps for d.ts files."""
    declarationMap: Optional[bool] = None
    """Output compiler performance information after building."""
    diagnostics: Optional[bool] = None
    """Reduce the number of projects loaded automatically by TypeScript."""
    disableReferencedProjectLoad: Optional[bool] = None
    """Remove the 20mb cap on total source code size for JavaScript files in the TypeScript
    language server.
    """
    disableSizeLimit: Optional[bool] = None
    """Opt a project out of multi-project reference checking when editing."""
    disableSolutionSearching: Optional[bool] = None
    """Disable preferring source files instead of declaration files when referencing composite
    projects
    """
    disableSourceOfProjectReferenceRedirect: Optional[bool] = None
    """Emit more compliant, but verbose and less performant JavaScript for iteration."""
    downlevelIteration: Optional[bool] = None
    """Emit a UTF-8 Byte Order Mark (BOM) in the beginning of output files."""
    emitBOM: Optional[bool] = None
    """Only output d.ts files and not JavaScript files."""
    emitDeclarationOnly: Optional[bool] = None
    """Emit design-type metadata for decorated declarations in source files."""
    emitDecoratorMetadata: Optional[bool] = None
    """Emit additional JavaScript to ease support for importing CommonJS modules. This enables
    `allowSyntheticDefaultImports` for type compatibility.
    """
    esModuleInterop: Optional[bool] = None
    """Differentiate between undefined and not present when type checking"""
    exactOptionalPropertyTypes: Optional[bool] = None
    """Enable experimental support for TC39 stage 2 draft decorators."""
    experimentalDecorators: Optional[bool] = None
    """Output more detailed compiler performance information after building."""
    extendedDiagnostics: Optional[bool] = None
    """Specify the polling strategy to use when the system runs out of or doesn't support native
    file watchers. Requires TypeScript version 3.8 or later.
    """
    fallbackPolling: Optional[FallbackPolling] = None
    """Ensure that casing is correct in imports."""
    forceConsistentCasingInFileNames: Optional[bool] = None
    """Emit a v8 CPU profile of the compiler run for debugging."""
    generateCpuProfile: Optional[str] = None
    """Allow importing helper functions from tslib once per project, instead of including them
    per-file.
    """
    importHelpers: Optional[bool] = None
    """Specify emit/checking behavior for imports that are only used for types."""
    importsNotUsedAsValues: Optional[ImportsNotUsedAsValues] = None
    """Enable incremental compilation. Requires TypeScript version 3.4 or later."""
    incremental: Optional[bool] = None
    """Include sourcemap files inside the emitted JavaScript."""
    inlineSourceMap: Optional[bool] = None
    """Include source code in the sourcemaps inside the emitted JavaScript."""
    inlineSources: Optional[bool] = None
    """Ensure that each file can be safely transpiled without relying on other imports."""
    isolatedModules: Optional[bool] = None
    """Specify what JSX code is generated."""
    jsx: Optional[Jsx] = None
    """Specify the JSX factory function used when targeting React JSX emit, e.g.
    'React.createElement' or 'h'
    """
    jsxFactory: Optional[str] = None
    """Specify the JSX Fragment reference used for fragments when targeting React JSX emit e.g.
    'React.Fragment' or 'Fragment'.
    """
    jsxFragmentFactory: Optional[str] = None
    """Specify module specifier used to import the JSX factory functions when using `jsx:
    react-jsx`.
    """
    jsxImportSource: Optional[str] = None
    """Make keyof only return strings instead of string, numbers or symbols. Legacy option."""
    keyofStringsOnly: Optional[bool] = None
    """Specify a set of bundled library declaration files that describe the target runtime
    environment.
    """
    lib: Optional[List[str]] = None
    """Print the names of emitted files after a compilation."""
    listEmittedFiles: Optional[bool] = None
    """Print all of the files read during the compilation."""
    listFiles: Optional[bool] = None
    """Print names of files that are part of the compilation and then stop processing."""
    listFilesOnly: Optional[bool] = None
    """Specify the location where debugger should locate map files instead of generated
    locations.
    """
    mapRoot: Optional[str] = None
    """Specify the maximum folder depth used for checking JavaScript files from `node_modules`.
    Only applicable with `allowJs`.
    """
    maxNodeModuleJsDepth: Optional[float] = None
    """Specify what module code is generated."""
    module: Optional[str] = None
    """Specify how TypeScript looks up a file from a given module specifier."""
    moduleResolution: Optional[str] = None
    """Set the newline character for emitting files."""
    newLine: Optional[str] = None
    """Disable emitting file from a compilation."""
    noEmit: Optional[bool] = None
    """Disable generating custom helper functions like `__extends` in compiled output."""
    noEmitHelpers: Optional[bool] = None
    """Disable emitting files if any type checking errors are reported."""
    noEmitOnError: Optional[bool] = None
    """Disable truncating types in error messages."""
    noErrorTruncation: Optional[bool] = None
    """Enable error reporting for fallthrough cases in switch statements."""
    noFallthroughCasesInSwitch: Optional[bool] = None
    """Enable error reporting for expressions and declarations with an implied `any` type.."""
    noImplicitAny: Optional[bool] = None
    """Ensure overriding members in derived classes are marked with an override modifier."""
    noImplicitOverride: Optional[bool] = None
    """Enable error reporting for codepaths that do not explicitly return in a function."""
    noImplicitReturns: Optional[bool] = None
    """Enable error reporting when `this` is given the type `any`."""
    noImplicitThis: Optional[bool] = None
    """Disable adding 'use strict' directives in emitted JavaScript files."""
    noImplicitUseStrict: Optional[bool] = None
    """Disable including any library files, including the default lib.d.ts."""
    noLib: Optional[bool] = None
    """Enforces using indexed accessors for keys declared using an indexed type"""
    noPropertyAccessFromIndexSignature: Optional[bool] = None
    """Disallow `import`s, `require`s or `<reference>`s from expanding the number of files
    TypeScript should add to a project.
    """
    noResolve: Optional[bool] = None
    """Disable strict checking of generic signatures in function types."""
    noStrictGenericChecks: Optional[bool] = None
    """Add `undefined` to a type when accessed using an index."""
    noUncheckedIndexedAccess: Optional[bool] = None
    """Enable error reporting when a local variables aren't read."""
    noUnusedLocals: Optional[bool] = None
    """Raise an error when a function parameter isn't read"""
    noUnusedParameters: Optional[bool] = None
    """Specify an output folder for all emitted files."""
    outDir: Optional[str] = None
    """Specify a file that bundles all outputs into one JavaScript file. If `declaration` is
    true, also designates a file that bundles all .d.ts output.
    """
    outFile: Optional[str] = None
    """Specify a set of entries that re-map imports to additional lookup locations."""
    paths: Optional[Dict[str, List[str]]] = None
    """Specify a list of language service plugins to include."""
    plugins: Optional[List[Plugin]] = None
    """Disable erasing `const enum` declarations in generated code."""
    preserveConstEnums: Optional[bool] = None
    """Disable resolving symlinks to their realpath. This correlates to the same flag in node."""
    preserveSymlinks: Optional[bool] = None
    """Preserve unused imported values in the JavaScript output that would otherwise be removed"""
    preserveValueImports: Optional[bool] = None
    """Disable wiping the console in watch mode"""
    preserveWatchOutput: Optional[bool] = None
    """Enable color and formatting in output to make compiler errors easier to read"""
    pretty: Optional[bool] = None
    """Specify the object invoked for `createElement`. This only applies when targeting `react`
    JSX emit.
    """
    reactNamespace: Optional[str] = None
    """Disable emitting comments."""
    removeComments: Optional[bool] = None
    """Enable importing .json files"""
    resolveJsonModule: Optional[bool] = None
    """Specify the root folder within your source files."""
    rootDir: Optional[str] = None
    """Allow multiple folders to be treated as one when resolving modules."""
    rootDirs: Optional[List[str]] = None
    """Skip type checking .d.ts files that are included with TypeScript."""
    skipDefaultLibCheck: Optional[bool] = None
    """Skip type checking all .d.ts files."""
    skipLibCheck: Optional[bool] = None
    """Create source map files for emitted JavaScript files."""
    sourceMap: Optional[bool] = None
    """Specify the root path for debuggers to find the reference source code."""
    sourceRoot: Optional[str] = None
    """Enable all strict type checking options."""
    strict: Optional[bool] = None
    """Check that the arguments for `bind`, `call`, and `apply` methods match the original
    function.
    """
    strictBindCallApply: Optional[bool] = None
    """When assigning functions, check to ensure parameters and the return values are
    subtype-compatible.
    """
    strictFunctionTypes: Optional[bool] = None
    """When type checking, take into account `null` and `undefined`."""
    strictNullChecks: Optional[bool] = None
    """Check for class properties that are declared but not set in the constructor."""
    strictPropertyInitialization: Optional[bool] = None
    """Disable emitting declarations that have `@internal` in their JSDoc comments."""
    stripInternal: Optional[bool] = None
    """Disable reporting of excess property errors during the creation of object literals."""
    suppressExcessPropertyErrors: Optional[bool] = None
    """Suppress `noImplicitAny` errors when indexing objects that lack index signatures."""
    suppressImplicitAnyIndexErrors: Optional[bool] = None
    """Set the JavaScript language version for emitted JavaScript and include compatible library
    declarations.
    """
    target: Optional[str] = None
    """Enable tracing of the name resolution process. Requires TypeScript version 2.0 or later."""
    traceResolution: Optional[bool] = None
    """Specify the folder for .tsbuildinfo incremental compilation files."""
    tsBuildInfoFile: Optional[str] = None
    """Specify multiple folders that act like `./node_modules/@types`."""
    typeRoots: Optional[List[str]] = None
    """Specify type package names to be included without being referenced in a source file."""
    types: Optional[List[str]] = None
    """Emit ECMAScript-standard-compliant class fields."""
    useDefineForClassFields: Optional[bool] = None
    """Default catch clause variables as `unknown` instead of `any`."""
    useUnknownInCatchVariables: Optional[bool] = None
    """Watch input files."""
    watch: Optional[bool] = None
    """Specify the strategy for watching directories under systems that lack recursive
    file-watching functionality. Requires TypeScript version 3.8 or later.
    """
    watchDirectory: Optional[WatchDirectory] = None
    """Specify the strategy for watching individual files. Requires TypeScript version 3.8 or
    later.
    """
    watchFile: Optional[WatchFile] = None


@dataclass
class Reference:
    """Project reference."""

    """Path to referenced tsconfig or to folder containing tsconfig."""
    path: Optional[str] = None


@dataclass
class TsNodeCompilerOptions:
    """JSON object to merge with TypeScript `compilerOptions`.

    Instructs the TypeScript compiler how to compile .ts files.
    """

    """Allow JavaScript files to be a part of your program. Use the `checkJS` option to get
    errors from these files.
    """
    allowJs: Optional[bool] = None
    """Allow 'import x from y' when a module doesn't have a default export."""
    allowSyntheticDefaultImports: Optional[bool] = None
    """Allow accessing UMD globals from modules."""
    allowUmdGlobalAccess: Optional[bool] = None
    """Disable error reporting for unreachable code."""
    allowUnreachableCode: Optional[bool] = None
    """Disable error reporting for unused labels."""
    allowUnusedLabels: Optional[bool] = None
    """Ensure 'use strict' is always emitted."""
    alwaysStrict: Optional[bool] = None
    """Have recompiles in '--incremental' and '--watch' assume that changes within a file will
    only affect files directly depending on it. Requires TypeScript version 3.8 or later.
    """
    assumeChangesOnlyAffectDirectDependencies: Optional[bool] = None
    """Specify the base directory to resolve non-relative module names."""
    baseUrl: Optional[str] = None
    """No longer supported. In early versions, manually set the text encoding for reading files."""
    charset: Optional[str] = None
    """Enable error reporting in type-checked JavaScript files."""
    checkJs: Optional[bool] = None
    """Enable constraints that allow a TypeScript project to be used with project references."""
    composite: Optional[bool] = None
    """Generate .d.ts files from my_typescript and JavaScript files in your project."""
    declaration: Optional[bool] = None
    """Specify the output directory for generated declaration files."""
    declarationDir: Optional[str] = None
    """Create sourcemaps for d.ts files."""
    declarationMap: Optional[bool] = None
    """Output compiler performance information after building."""
    diagnostics: Optional[bool] = None
    """Reduce the number of projects loaded automatically by TypeScript."""
    disableReferencedProjectLoad: Optional[bool] = None
    """Remove the 20mb cap on total source code size for JavaScript files in the TypeScript
    language server.
    """
    disableSizeLimit: Optional[bool] = None
    """Opt a project out of multi-project reference checking when editing."""
    disableSolutionSearching: Optional[bool] = None
    """Disable preferring source files instead of declaration files when referencing composite
    projects
    """
    disableSourceOfProjectReferenceRedirect: Optional[bool] = None
    """Emit more compliant, but verbose and less performant JavaScript for iteration."""
    downlevelIteration: Optional[bool] = None
    """Emit a UTF-8 Byte Order Mark (BOM) in the beginning of output files."""
    emitBOM: Optional[bool] = None
    """Only output d.ts files and not JavaScript files."""
    emitDeclarationOnly: Optional[bool] = None
    """Emit design-type metadata for decorated declarations in source files."""
    emitDecoratorMetadata: Optional[bool] = None
    """Emit additional JavaScript to ease support for importing CommonJS modules. This enables
    `allowSyntheticDefaultImports` for type compatibility.
    """
    esModuleInterop: Optional[bool] = None
    """Differentiate between undefined and not present when type checking"""
    exactOptionalPropertyTypes: Optional[bool] = None
    """Enable experimental support for TC39 stage 2 draft decorators."""
    experimentalDecorators: Optional[bool] = None
    """Output more detailed compiler performance information after building."""
    extendedDiagnostics: Optional[bool] = None
    """Specify the polling strategy to use when the system runs out of or doesn't support native
    file watchers. Requires TypeScript version 3.8 or later.
    """
    fallbackPolling: Optional[FallbackPolling] = None
    """Ensure that casing is correct in imports."""
    forceConsistentCasingInFileNames: Optional[bool] = None
    """Emit a v8 CPU profile of the compiler run for debugging."""
    generateCpuProfile: Optional[str] = None
    """Allow importing helper functions from tslib once per project, instead of including them
    per-file.
    """
    importHelpers: Optional[bool] = None
    """Specify emit/checking behavior for imports that are only used for types."""
    importsNotUsedAsValues: Optional[ImportsNotUsedAsValues] = None
    """Enable incremental compilation. Requires TypeScript version 3.4 or later."""
    incremental: Optional[bool] = None
    """Include sourcemap files inside the emitted JavaScript."""
    inlineSourceMap: Optional[bool] = None
    """Include source code in the sourcemaps inside the emitted JavaScript."""
    inlineSources: Optional[bool] = None
    """Ensure that each file can be safely transpiled without relying on other imports."""
    isolatedModules: Optional[bool] = None
    """Specify what JSX code is generated."""
    jsx: Optional[Jsx] = None
    """Specify the JSX factory function used when targeting React JSX emit, e.g.
    'React.createElement' or 'h'
    """
    jsxFactory: Optional[str] = None
    """Specify the JSX Fragment reference used for fragments when targeting React JSX emit e.g.
    'React.Fragment' or 'Fragment'.
    """
    jsxFragmentFactory: Optional[str] = None
    """Specify module specifier used to import the JSX factory functions when using `jsx:
    react-jsx`.
    """
    jsxImportSource: Optional[str] = None
    """Make keyof only return strings instead of string, numbers or symbols. Legacy option."""
    keyofStringsOnly: Optional[bool] = None
    """Specify a set of bundled library declaration files that describe the target runtime
    environment.
    """
    lib: Optional[List[str]] = None
    """Print the names of emitted files after a compilation."""
    listEmittedFiles: Optional[bool] = None
    """Print all of the files read during the compilation."""
    listFiles: Optional[bool] = None
    """Print names of files that are part of the compilation and then stop processing."""
    listFilesOnly: Optional[bool] = None
    """Specify the location where debugger should locate map files instead of generated
    locations.
    """
    mapRoot: Optional[str] = None
    """Specify the maximum folder depth used for checking JavaScript files from `node_modules`.
    Only applicable with `allowJs`.
    """
    maxNodeModuleJsDepth: Optional[float] = None
    """Specify what module code is generated."""
    module: Optional[str] = None
    """Specify how TypeScript looks up a file from a given module specifier."""
    moduleResolution: Optional[str] = None
    """Set the newline character for emitting files."""
    newLine: Optional[str] = None
    """Disable emitting file from a compilation."""
    noEmit: Optional[bool] = None
    """Disable generating custom helper functions like `__extends` in compiled output."""
    noEmitHelpers: Optional[bool] = None
    """Disable emitting files if any type checking errors are reported."""
    noEmitOnError: Optional[bool] = None
    """Disable truncating types in error messages."""
    noErrorTruncation: Optional[bool] = None
    """Enable error reporting for fallthrough cases in switch statements."""
    noFallthroughCasesInSwitch: Optional[bool] = None
    """Enable error reporting for expressions and declarations with an implied `any` type.."""
    noImplicitAny: Optional[bool] = None
    """Ensure overriding members in derived classes are marked with an override modifier."""
    noImplicitOverride: Optional[bool] = None
    """Enable error reporting for codepaths that do not explicitly return in a function."""
    noImplicitReturns: Optional[bool] = None
    """Enable error reporting when `this` is given the type `any`."""
    noImplicitThis: Optional[bool] = None
    """Disable adding 'use strict' directives in emitted JavaScript files."""
    noImplicitUseStrict: Optional[bool] = None
    """Disable including any library files, including the default lib.d.ts."""
    noLib: Optional[bool] = None
    """Enforces using indexed accessors for keys declared using an indexed type"""
    noPropertyAccessFromIndexSignature: Optional[bool] = None
    """Disallow `import`s, `require`s or `<reference>`s from expanding the number of files
    TypeScript should add to a project.
    """
    noResolve: Optional[bool] = None
    """Disable strict checking of generic signatures in function types."""
    noStrictGenericChecks: Optional[bool] = None
    """Add `undefined` to a type when accessed using an index."""
    noUncheckedIndexedAccess: Optional[bool] = None
    """Enable error reporting when a local variables aren't read."""
    noUnusedLocals: Optional[bool] = None
    """Raise an error when a function parameter isn't read"""
    noUnusedParameters: Optional[bool] = None
    """Specify an output folder for all emitted files."""
    outDir: Optional[str] = None
    """Specify a file that bundles all outputs into one JavaScript file. If `declaration` is
    true, also designates a file that bundles all .d.ts output.
    """
    outFile: Optional[str] = None
    """Specify a set of entries that re-map imports to additional lookup locations."""
    paths: Optional[Dict[str, List[str]]] = None
    """Specify a list of language service plugins to include."""
    plugins: Optional[List[Plugin]] = None
    """Disable erasing `const enum` declarations in generated code."""
    preserveConstEnums: Optional[bool] = None
    """Disable resolving symlinks to their realpath. This correlates to the same flag in node."""
    preserveSymlinks: Optional[bool] = None
    """Preserve unused imported values in the JavaScript output that would otherwise be removed"""
    preserveValueImports: Optional[bool] = None
    """Disable wiping the console in watch mode"""
    preserveWatchOutput: Optional[bool] = None
    """Enable color and formatting in output to make compiler errors easier to read"""
    pretty: Optional[bool] = None
    """Specify the object invoked for `createElement`. This only applies when targeting `react`
    JSX emit.
    """
    reactNamespace: Optional[str] = None
    """Disable emitting comments."""
    removeComments: Optional[bool] = None
    """Enable importing .json files"""
    resolveJsonModule: Optional[bool] = None
    """Specify the root folder within your source files."""
    rootDir: Optional[str] = None
    """Allow multiple folders to be treated as one when resolving modules."""
    rootDirs: Optional[List[str]] = None
    """Skip type checking .d.ts files that are included with TypeScript."""
    skipDefaultLibCheck: Optional[bool] = None
    """Skip type checking all .d.ts files."""
    skipLibCheck: Optional[bool] = None
    """Create source map files for emitted JavaScript files."""
    sourceMap: Optional[bool] = None
    """Specify the root path for debuggers to find the reference source code."""
    sourceRoot: Optional[str] = None
    """Enable all strict type checking options."""
    strict: Optional[bool] = None
    """Check that the arguments for `bind`, `call`, and `apply` methods match the original
    function.
    """
    strictBindCallApply: Optional[bool] = None
    """When assigning functions, check to ensure parameters and the return values are
    subtype-compatible.
    """
    strictFunctionTypes: Optional[bool] = None
    """When type checking, take into account `null` and `undefined`."""
    strictNullChecks: Optional[bool] = None
    """Check for class properties that are declared but not set in the constructor."""
    strictPropertyInitialization: Optional[bool] = None
    """Disable emitting declarations that have `@internal` in their JSDoc comments."""
    stripInternal: Optional[bool] = None
    """Disable reporting of excess property errors during the creation of object literals."""
    suppressExcessPropertyErrors: Optional[bool] = None
    """Suppress `noImplicitAny` errors when indexing objects that lack index signatures."""
    suppressImplicitAnyIndexErrors: Optional[bool] = None
    """Set the JavaScript language version for emitted JavaScript and include compatible library
    declarations.
    """
    target: Optional[str] = None
    """Enable tracing of the name resolution process. Requires TypeScript version 2.0 or later."""
    traceResolution: Optional[bool] = None
    """Specify the folder for .tsbuildinfo incremental compilation files."""
    tsBuildInfoFile: Optional[str] = None
    """Specify multiple folders that act like `./node_modules/@types`."""
    typeRoots: Optional[List[str]] = None
    """Specify type package names to be included without being referenced in a source file."""
    types: Optional[List[str]] = None
    """Emit ECMAScript-standard-compliant class fields."""
    useDefineForClassFields: Optional[bool] = None
    """Default catch clause variables as `unknown` instead of `any`."""
    useUnknownInCatchVariables: Optional[bool] = None
    """Watch input files."""
    watch: Optional[bool] = None
    """Specify the strategy for watching directories under systems that lack recursive
    file-watching functionality. Requires TypeScript version 3.8 or later.
    """
    watchDirectory: Optional[WatchDirectory] = None
    """Specify the strategy for watching individual files. Requires TypeScript version 3.8 or
    later.
    """
    watchFile: Optional[WatchFile] = None


class ExperimentalSpecifierResolution(Enum):
    """Like node's `--experimental-specifier-resolution`, , but can also be set in your
    `tsconfig.json` for convenience.

    For details, see
    https://nodejs.org/dist/latest-v18.x/docs/api/esm.html#customizing-esm-specifier-resolution-algorithm
    """

    explicit = "explicit"
    node = "node"


@dataclass
class TsNode:
    """ts-node options.  See also: https://typestrong.org/ts-node/docs/configuration

    ts-node offers TypeScript execution and REPL for node.js, with source map support.
    """

    """Specify a custom transpiler for use with transpileOnly"""
    transpiler: Optional[Union[List[Union[Dict[str, Any], str]], str]] = None
    """Specify a custom TypeScript compiler."""
    compiler: Optional[str] = None
    """Use TypeScript's compiler host API instead of the language service API."""
    compilerHost: Optional[bool] = None
    """JSON object to merge with TypeScript `compilerOptions`."""
    compilerOptions: Optional[TsNodeCompilerOptions] = None
    """Emit output files into `.ts-node` directory."""
    emit: Optional[bool] = None
    """Enable native ESM support.

    For details, see https://typestrong.org/ts-node/docs/imports#native-ecmascript-modules
    """
    esm: Optional[bool] = None
    """Allows the usage of top level await in REPL.

    Uses node's implementation which accomplishes this with an AST syntax transformation.

    Enabled by default when tsconfig target is es2018 or above. Set to false to disable.

    **Note**: setting to `true` when tsconfig target is too low will throw an Error.  Leave
    as `undefined`
    to get default, automatic behavior.
    """
    experimentalReplAwait: Optional[bool] = None
    """Enable experimental features that re-map imports and require calls to support:
    `baseUrl`, `paths`, `rootDirs`, `.js` to `.ts` file extension mappings,
    `outDir` to `rootDir` mappings for composite projects and monorepos.

    For details, see https://github.com/TypeStrong/ts-node/issues/1514
    """
    experimentalResolver: Optional[bool] = None
    """Like node's `--experimental-specifier-resolution`, , but can also be set in your
    `tsconfig.json` for convenience.

    For details, see
    https://nodejs.org/dist/latest-v18.x/docs/api/esm.html#customizing-esm-specifier-resolution-algorithm
    """
    experimentalSpecifierResolution: Optional[
        ExperimentalSpecifierResolution
    ] = None
    """Allow using voluntary `.ts` file extension in import specifiers.

    Typically, in ESM projects, import specifiers must have an emit extension, `.js`, `.cjs`,
    or `.mjs`,
    and we automatically map to the corresponding `.ts`, `.cts`, or `.mts` source file.  This
    is the
    recommended approach.

    However, if you really want to use `.ts` in import specifiers, and are aware that this
    may
    break tooling, you can enable this flag.
    """
    experimentalTsImportSpecifiers: Optional[bool] = None
    """Load "files" and "include" from `tsconfig.json` on startup.

    Default is to override `tsconfig.json` "files" and "include" to only include the
    entrypoint script.
    """
    files: Optional[bool] = None
    """Paths which should not be compiled.

    Each string in the array is converted to a regular expression via `new RegExp()` and
    tested against source paths prior to compilation.

    Source paths are normalized to posix-style separators, relative to the directory
    containing `tsconfig.json` or to cwd if no `tsconfig.json` is loaded.

    Default is to ignore all node_modules subdirectories.
    """
    ignore: Optional[List[str]] = None
    """Ignore TypeScript warnings by diagnostic code."""
    ignoreDiagnostics: Optional[List[Union[float, str]]] = None
    """Logs TypeScript errors to stderr instead of throwing exceptions."""
    logError: Optional[bool] = None
    """Override certain paths to be compiled and executed as CommonJS or ECMAScript modules.
    When overridden, the tsconfig "module" and package.json "type" fields are overridden, and
    the file extension is ignored.
    This is useful if you cannot use .mts, .cts, .mjs, or .cjs file extensions;
    it achieves the same effect.

    Each key is a glob pattern following the same rules as tsconfig's "include" array.
    When multiple patterns match the same file, the last pattern takes precedence.

    `cjs` overrides matches files to compile and execute as CommonJS.
    `esm` overrides matches files to compile and execute as native ECMAScript modules.
    `package` overrides either of the above to default behavior, which obeys package.json
    "type" and
    tsconfig.json "module" options.
    """
    moduleTypes: Optional[Dict[str, Any]] = None
    """Re-order file extensions so that TypeScript imports are preferred.

    For example, when both `index.js` and `index.ts` exist, enabling this option causes
    `require('./index')` to resolve to `index.ts` instead of `index.js`
    """
    preferTsExts: Optional[bool] = None
    """Use pretty diagnostic formatter."""
    pretty: Optional[bool] = None
    """Modules to require, like node's `--require` flag.

    If specified in `tsconfig.json`, the modules will be resolved relative to the
    `tsconfig.json` file.

    If specified programmatically, each input string should be pre-resolved to an absolute
    path for
    best results.
    """
    require: Optional[List[str]] = None
    """Scope compiler to files within `scopeDir`."""
    scope: Optional[bool] = None
    scopeDir: Optional[str] = None
    """Skip ignore check, so that compilation will be attempted for all files with matching
    extensions.
    """
    skipIgnore: Optional[bool] = None
    """Transpile with swc instead of the TypeScript compiler, and skip typechecking.

    Equivalent to setting both `transpileOnly: true` and `transpiler:
    'ts-node/transpilers/swc'`

    For complete instructions: https://typestrong.org/ts-node/docs/transpilers
    """
    swc: Optional[bool] = None
    """Use TypeScript's faster `transpileModule`."""
    transpileOnly: Optional[bool] = None
    """**DEPRECATED** Specify type-check is enabled (e.g. `transpileOnly == false`)."""
    typeCheck: Optional[bool] = None


@dataclass
class TypeAcquisition:
    """Auto type (.d.ts) acquisition options for this project. Requires TypeScript version 2.1
    or later.
    """

    """Enable auto type acquisition"""
    enable: Optional[bool] = None
    """Specifies a list of type declarations to be excluded from auto type acquisition. Ex.
    ["jquery", "lodash"]
    """
    exclude: Optional[List[str]] = None
    """Specifies a list of type declarations to be included in auto type acquisition. Ex.
    ["jquery", "lodash"]
    """
    include: Optional[List[str]] = None


@dataclass
class WatchOptions:
    """Settings for the watch mode in TypeScript."""

    """Remove a list of directories from the watch process."""
    excludeDirectories: Optional[List[str]] = None
    """Remove a list of files from the watch mode's processing."""
    excludeFiles: Optional[List[str]] = None
    """Specify what approach the watcher should use if the system runs out of native file
    watchers.
    """
    fallbackPolling: Optional[str] = None
    """~"""
    force: Optional[str] = None
    """Synchronously call callbacks and update the state of directory watchers on platforms that
    don`t support recursive watching natively.
    """
    synchronousWatchDirectory: Optional[bool] = None
    """Specify how directories are watched on systems that lack recursive file-watching
    functionality.
    """
    watchDirectory: Optional[str] = None
    """Specify how the TypeScript watch mode works."""
    watchFile: Optional[str] = None


@dataclass
class TSConfig:
    buildOptions: Optional[
        Union[float, int, bool, str, List[Any], BuildOptionsClass]
    ] = None
    """Instructs the TypeScript compiler how to compile .ts files."""
    compilerOptions: Optional[TSConfigCompilerOptions] = None
    """Enable Compile-on-Save for this project."""
    compileOnSave: Optional[bool] = None
    """Auto type (.d.ts) acquisition options for this project. Requires TypeScript version 2.1
    or later.
    """
    typeAcquisition: Optional[TypeAcquisition] = None
    """Path to base configuration file to inherit from. Requires TypeScript version 2.1 or later."""
    extends: Optional[str] = None
    """Settings for the watch mode in TypeScript."""
    watchOptions: Optional[WatchOptions] = None
    """ts-node options.  See also: https://typestrong.org/ts-node/docs/configuration

    ts-node offers TypeScript execution and REPL for node.js, with source map support.
    """
    tsnode: Optional[TsNode] = None
    """If no 'files' or 'include' property is present in a tsconfig.json, the compiler defaults
    to including all files in the containing directory and subdirectories except those
    specified by 'exclude'. When a 'files' property is specified, only those files and those
    specified by 'include' are included.
    """
    files: Optional[List[str]] = None
    """Specifies a list of files to be excluded from compilation. The 'exclude' property only
    affects the files included via the 'include' property and not the 'files' property. Glob
    patterns require TypeScript version 2.0 or later.
    """
    exclude: Optional[List[str]] = None
    """Specifies a list of glob patterns that match files to be included in compilation. If no
    'files' or 'include' property is present in a tsconfig.json, the compiler defaults to
    including all files in the containing directory and subdirectories except those specified
    by 'exclude'. Requires TypeScript version 2.0 or later.
    """
    include: Optional[List[str]] = None
    """Referenced projects. Requires TypeScript version 3.0 or later."""
    references: Optional[List[Reference]] = None
