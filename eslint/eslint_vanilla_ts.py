from my_types import Rules, ESLINT_TYPE
from eslint_vanilla import ESLINT_VANILLA, eslintignore

eslint_vanilla_ts: ESLINT_TYPE = ESLINT_VANILLA.copy()

eslint_vanilla_ts_rules: Rules = {
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
}

if "env" in eslint_vanilla_ts:
    del eslint_vanilla_ts["env"]["es2022"]

if "extends" in eslint_vanilla_ts:
    eslint_vanilla_ts["extends"].remove("airbnb-base")
    eslint_vanilla_ts["extends"].remove("plugin:prettier/recommended")
    eslint_vanilla_ts["extends"].extend(
        [
            "plugin:@typescript-eslint/eslint-recommended",
            "airbnb-base",
            "airbnb-typescript/base",
            "plugin:@typescript-eslint/recommended",
            "plugin:@typescript-eslint/recommended-requiring-type-checking",
            "plugin:@typescript-eslint/strict",
            "plugin:prettier/recommended",
        ]
    )

if "parserOptions" in eslint_vanilla_ts:
    eslint_vanilla_ts["parserOptions"]["project"] = ["./tsconfig.json"]
    eslint_vanilla_ts["parserOptions"]["tsconfigRootDir"] = "./"
if "plugins" in eslint_vanilla_ts:
    eslint_vanilla_ts["plugins"].insert(0, "@typescript-eslint")
if "rules" in eslint_vanilla_ts:
    eslint_vanilla_ts["rules"] = {
        **eslint_vanilla_ts["rules"],
        **eslint_vanilla_ts_rules,
    }
    # eslint_vanilla_ts["rules"].update(eslint_vanilla_ts_rules)
    # print((eslint_vanilla_ts["rules"]["prettier/prettier"][1]))
    if (
        "prettier/prettier" in eslint_vanilla_ts["rules"]
        and type(eslint_vanilla_ts["rules"]["prettier/prettier"]) is tuple
        and len(eslint_vanilla_ts["rules"]["prettier/prettier"]) == 2
    ):
        if type(eslint_vanilla_ts["rules"]["prettier/prettier"][1]) is dict:
            eslint_vanilla_ts["rules"]["prettier/prettier"][1][
                "parser"
            ] = "typescript"

eslintignore_ts = eslintignore
