from write_to_all_files import write_to_all_files


class File:
    def __init__(self, name: str, ext: str, folder: str, contents: str) -> None:
        self.name = name
        self.contents = contents
        self.ext = ext
        self.folder = folder
        self.directory = f"{folder}{name}.{ext}"

    def create_file(self) -> None:
        write_to_all_files([(self.directory, self.contents)])


class File_In_Current_Dir(File):
    def __init__(self, name: str, ext: str, contents: str) -> None:
        self.folder = ""
        super().__init__(name, ext, self.folder, contents)


class TS_File(File):
    def __init__(self, name: str, folder: str, contents: str) -> None:
        self.ext = "ts"
        super().__init__(name, self.ext, folder, contents)


class HTML_File(File_In_Current_Dir):
    def __init__(self, name: str, contents: str) -> None:
        self.ext = "html"
        super().__init__(name, self.ext, contents)


class Util_Function(TS_File):
    def __init__(self, name: str, contents: str) -> None:
        self.folder = "src/utils/"
        super().__init__(name, self.folder, contents)


class Custom_Hook(TS_File):
    def __init__(self, name: str, contents: str) -> None:
        self.folder = "src/hooks/"
        super().__init__(name, self.folder, contents)


class TSX_File(File):
    def __init__(self, name: str, folder: str, contents: str) -> None:
        self.ext = "tsx"
        super().__init__(name, self.ext, folder, contents)


class React_Component_In_SRC_Folder(TSX_File):
    def __init__(self, name: str, contents: str) -> None:
        self.folder = "src/"
        super().__init__(name, self.folder, contents)
