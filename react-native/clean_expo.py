from react.create_custom_hooks import create_custom_hooks
from clean_rn_app import clean_rn_app
from create_folder_react_native_ts import create_folder_react_native_ts
from write_to_file import write_to_all_files
from react.custom_hooks import useComponentStatus, useValueUpdateLogger


def clean_expo() -> None:
    create_folder_react_native_ts()
    create_custom_hooks([useComponentStatus, useValueUpdateLogger])
    write_to_all_files(
        [
            ("App.tsx", clean_rn_app),
            (
                "src/types/missingTypes.ts",
                "export type AnyObject = Record<string, unknown>;",
            ),
        ]
    )


if __name__ == "__main__":
    clean_expo()
