# settings: tuple[str, str] = (
#     ".vscode/settings.json",
#     """{
#   "editor.defaultFormatter": "dbaeumer.vscode-eslint",
#   "editor.formatOnSave": true,
#   "editor.codeActionsOnSave": {
#     "source.fixAll": true,
#     "source.addMissingImports": true,
#     "source.organizeImports": true
#   },
#   "[json]": {
#     "editor.defaultFormatter": "esbenp.prettier-vscode",
#     "editor.formatOnSave": true
#   },
#   "[jsonc]": {
#     "editor.defaultFormatter": "esbenp.prettier-vscode",
#     "editor.formatOnSave": true
#   }
# }
# """,
# )

from create_file import SETTINGS_JSON

settings = SETTINGS_JSON(
    {
        "editor.defaultFormatter": "dbaeumer.vscode-eslint",
        "editor.formatOnSave": True,
        "editor.codeActionsOnSave": {
            "source.fixAll": True,
            "source.addMissingImports": True,
            "source.organizeImports": True,
        },
        "[json]": {
            "editor.defaultFormatter": "esbenp.prettier-vscode",
            "editor.formatOnSave": True,
        },
        "[jsonc]": {
            "editor.defaultFormatter": "esbenp.prettier-vscode",
            "editor.formatOnSave": True,
        },
    }
)
