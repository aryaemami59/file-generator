import sys
from json import dump
from write_to_all_files import write_to_all_files
from eslint.my_types import ESLINT_TYPE, TS_CONFIG_TYPE
from typing import Literal, TypedDict, Any, Dict
from create_folder import create_folder
# from eslint.kk import TSConfig

ext_type = Literal["ts", "js", "json", "html", "css", "tsx", "jsx", "py", ""]


class Any_File:
    def __init__(
        self,
        name: str,
        ext: ext_type,
        folder: str,
        contents: Any,
    ) -> None:
        self.name = name
        self.contents = contents
        self.ext = ext
        self.folder = folder
        self.directory = f"{folder}{name}.{ext}"

    def info(self) -> None:
        print(
            f"name: {self.name}, extension: {self.ext}, "
            f"folder: {self.folder}, contents: {self.contents}"
        )


class File(Any_File):
    def __init__(
        self,
        name: str,
        ext: ext_type,
        folder: str,
        contents: str,
    ) -> None:
        super().__init__(name, ext, folder, contents)

    def create_file(self) -> None:
        write_to_all_files([(self.directory, self.contents)])


class File_In_Current_Dir(File):
    def __init__(self, name: str, ext: ext_type, contents: str) -> None:
        super().__init__(name, ext, "", contents)


class TS_File(File):
    def __init__(self, name: str, folder: str, contents: str) -> None:
        super().__init__(name, "ts", folder, contents)


class Empty_File(File):
    def __init__(self, name: str, ext: ext_type, folder: str) -> None:
        super().__init__(name, ext, folder, "")


class Empty_File_Current_Dir(Empty_File):
    def __init__(self, name: str, ext: ext_type) -> None:
        super().__init__(name, ext, "")


class Python_File(Empty_File):
    # print(sys.argv)

    def __init__(self, folder: str) -> None:
        super().__init__(sys.argv[1], "py", folder)

    # def create_file(self) -> None:
    #     write_to_all_files([(self.directory, self.contents)])


class HTML_File_Current_Dir(File_In_Current_Dir):
    ext: ext_type = "html"

    def __init__(self, name: str, contents: str) -> None:
        super().__init__(name, HTML_File_Current_Dir.ext, contents)


class CSS_File_Current_Dir(File_In_Current_Dir):
    ext: ext_type = "css"

    def __init__(self, name: str, contents: str) -> None:
        super().__init__(name, CSS_File_Current_Dir.ext, contents)


class Index_HTML_File(HTML_File_Current_Dir):
    def __init__(self, contents: str) -> None:
        super().__init__("index", contents)


class Styles_CSS_File(CSS_File_Current_Dir):
    def __init__(self, contents: str) -> None:
        super().__init__("styles", contents)


class Util_Function(TS_File):
    def __init__(self, name: str, contents: str) -> None:
        super().__init__(name, "src/utils/", contents)


class Custom_Hook(TS_File):
    def __init__(self, name: str, contents: str) -> None:
        super().__init__(name, "src/hooks/", contents)


class Logger_Hook(TS_File):
    def __init__(self, name: str, contents: str) -> None:
        super().__init__(name, "src/hooks/loggers/", contents)


class TSX_File(File):
    def __init__(self, name: str, folder: str, contents: str) -> None:
        super().__init__(name, "tsx", folder, contents)


class React_Component_In_SRC_Folder(TSX_File):
    def __init__(self, name: str, contents: str) -> None:
        super().__init__(name, "src/", contents)


class JSON_File(Any_File):
    def __init__(self, name: str, folder: str, contents: TypedDict) -> None:
        super().__init__(name, "json", folder, contents)

    def create_file(self) -> None:
        file = open(f"{self.name}.{self.ext}", "w")
        dump(self.contents, file, indent=2, sort_keys=True)
        file.close()


class ESLINT_RC_JSON(JSON_File):
    def __init__(self, contents: ESLINT_TYPE) -> None:
        super().__init__(".eslintrc", "", contents)


class SETTINGS_JSON(Any_File):
    def __init__(self, contents: Dict[str, Any]) -> None:
        super().__init__("settings", "json", ".vscode/", contents)

    def create_file(self) -> None:
        create_folder([".vscode"])
        file = open(f"{self.directory}", "w")
        dump(self.contents, file, indent=2, sort_keys=True)
        file.close()


class TS_CONFIG_JSON(JSON_File):
    def __init__(self, contents: TS_CONFIG_TYPE) -> None:
        super().__init__("tsconfig", "", contents)


class Ignore_Files(File):
    def __init__(
        self,
        name: str,
        folder: str,
        contents: str,
    ) -> None:
        super().__init__(name, "", folder, contents)


class ESLINT_Ignore(Ignore_Files):
    def __init__(
        self,
        contents: str,
    ) -> None:
        super().__init__(".eslintignore", "", contents)


# import platform
# print(platform.python_version())

# from pydantic import BaseModel

# # Define your TypeScript interface as a string
# typescript_interface = 'interface Person {name: string;age: number;city: string;}'


# # Parse the TypeScript interface into a Pydantic BaseModel class
# Person = BaseModel.parse_raw(typescript_interface)

# # Print the resulting TypedDict class
# print(Person)
