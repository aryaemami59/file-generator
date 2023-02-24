eslint_vanilla = {
    "env": {"browser": True, "es2022": True},
    "extends": ["eslint:recommended", "airbnb-base", "plugin:prettier/recommended"],
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
