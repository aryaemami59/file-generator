eslint_react_ts = {
    "env": {"browser": True, "es2022": True},
    "extends": [
        "eslint:recommended",
        "plugin:@typescript-eslint/eslint-recommended",
        "plugin:@typescript-eslint/recommended",
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
        "prettier/prettier",
        "plugin:prettier/recommended",
    ],
    "overrides": [],
    "parser": "@typescript-eslint/parser",
    "parserOptions": {
        "ecmaFeatures": {"jsx": True},
        "ecmaVersion": "latest",
        "project": ["./tsconfig.json"],
        "sourceType": "module",
        "tsconfigRootDir": "./",
    },
    "plugins": [
        "react",
        "@typescript-eslint",
        "eslint-plugin-prettier",
        "react-perf",
        "prefer-arrow-functions",
        "prettier",
        "jsx-a11y",
    ],
    "root": True,
    "rules": {
        "@typescript-eslint/ban-ts-comment": [0],
        "@typescript-eslint/consistent-type-definitions": [2, "type"],
        "@typescript-eslint/consistent-type-imports": [2],
        "@typescript-eslint/naming-convention": [0],
        "@typescript-eslint/no-floating-promises": [0],
        "@typescript-eslint/no-throw-literal": [0],
        "no-console": 0,
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
                "parser": "typescript",
                "singleAttributePerLine": True,
            },
        ],
        "react/function-component-definition": [
            2,
            {
                "namedComponents": "arrow-function",
                "unnamedComponents": "arrow-function",
            },
        ],
        "react/jsx-props-no-spreading": [0],
        "react/require-default-props": [0],
    },
    "settings": {"react": {"version": "detect"}},
}

eslintignore_react = "node_modules\nbuild\n.git\n.vscode\npublic\nnetlify.toml\ntsconfig.json\nvite.config.ts"
