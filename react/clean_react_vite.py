from clean_react_vite_app import clean_react_vite_app
from clean_react_vite_main import clean_react_vite_main
from clean_react_index_html import clean_react_index_html
from create_custom_hooks import create_custom_hooks
from create_folder_react_ts import create_folder_react_ts
from custom_hooks import useComponentStatus, useValueUpdateLogger
from write_to_all_files import write_to_all_files
import os


def clean_react_vite() -> None:
    create_folder_react_ts()
    create_custom_hooks([useComponentStatus, useValueUpdateLogger])
    write_to_all_files(
        [
            ("src/App.tsx", clean_react_vite_app),
            ("src/main.tsx", clean_react_vite_main),
            ("index.html", clean_react_index_html),
            ("src/App.css", ""),
            ("README.md", "# New Project"),
            (
                "src/types/missingTypes.ts",
                "export type AnyObject = Record<string, unknown>;",
            ),
        ]
    )
    os.remove("src/index.css")
    os.remove("src/assets/react.svg")
    os.remove("public/vite.svg")


if __name__ == "__main__":
    clean_react_vite()
