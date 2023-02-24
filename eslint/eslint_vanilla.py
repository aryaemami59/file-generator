eslint_vanilla = {
    "env": {"browser": True, "es2022": True},
    "extends": [
        "eslint:recommended",
        "plugin:@typescript-eslint/eslint-recommended",
        "plugin:@typescript-eslint/recommended",
        "airbnb",
        "airbnb-typescript",
        "airbnb/hooks",
        "plugin:jsx-a11y/strict",
        "plugin:@typescript-eslint/recommended",
        "plugin:@typescript-eslint/recommended-requiring-type-checking",
        "plugin:@typescript-eslint/strict",
        "plugin:prettier/recommended",
    ],
    "overrides": [],
    "parser": "@typescript-eslint/parser",
    "parserOptions": {
        "ecmaVersion": "latest",
        "project": ["./tsconfig.json"],
        "sourceType": "module",
        "tsconfigRootDir": "./",
    },
    "plugins": [
        "@typescript-eslint",
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
                "parser": "typescript",
                "singleAttributePerLine": True,
            },
        ],
    },
}

eslintignore = "node_modules\n.vscode\ntsconfig.json"
