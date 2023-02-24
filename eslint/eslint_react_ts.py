eslint_react_ts = {
    "parser": "@typescript-eslint/parser",
    "parserOptions": {
        "project": ["./tsconfig.json"],
        "sourceType": "module",
        "ecmaVersion": "latest",
        "ecmaFeatures": {"jsx": True},
        "tsconfigRootDir": "./",
    },
    "plugins": [
        "react",
        "@typescript-eslint",
        "prefer-arrow",
        "react-perf",
        "prettier",
        "react-redux",
        "jsx-a11y",
    ],
    "extends": [
        "eslint:recommended",
        "plugin:@typescript-eslint/eslint-recommended",
        "airbnb",
        "airbnb-typescript",
        "airbnb/hooks",
        "react-app",
        "plugin:react/recommended",
        "plugin:react/jsx-runtime",
        "plugin:jsx-a11y/strict",
        "plugin:react-redux/all",
        "plugin:react-perf/all",
        "plugin:@typescript-eslint/recommended",
        "plugin:@typescript-eslint/recommended-requiring-type-checking",
        "plugin:@typescript-eslint/strict",
        "plugin:prettier/recommended",
    ],
    "env": {"browser": True, "es2022": True},
    "rules": {
        "prettier/prettier": [
            2,
            {
                "bracketSameLine": True,
                "arrowParens": "avoid",
                "singleAttributePerLine": True,
                "parser": "typescript",
            },
        ],
        "react/function-component-definition": [
            2,
            {
                "namedComponents": "arrow-function",
                "unnamedComponents": "arrow-function",
            },
        ],
        "no-console": [0],
        "no-param-reassign": [2, {"props": False}],
        "prefer-arrow/prefer-arrow-functions": [2],
        "@typescript-eslint/no-floating-promises": [0],
        "react/jsx-props-no-spreading": [0],
        "@typescript-eslint/consistent-type-imports": [2],
        "react/require-default-props": [0],
        "@typescript-eslint/no-throw-literal": [0],
        "@typescript-eslint/naming-convention": [
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
                "selector": ["objectLiteralProperty"],
                "modifiers": ["requiresQuotes"],
            },
            {"format": ["camelCase"], "selector": ["parameter"]},
        ],
        "@typescript-eslint/consistent-type-definitions": [2, "type"],
    },
    "settings": {"react": {"version": "detect"}},
    "root": True,
}


eslintignore_react = "node_modules\nbuild\n.git\n.vscode\npublic\nnetlify.toml\ntsconfig.json\nvite.config.ts"
