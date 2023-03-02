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

    def info(self) -> None:
        print(
            f"name: {self.name}, extension: {self.ext}, folder: {self.folder}, contents: {self.contents}"
        )


class File_In_Current_Dir(File):
    def __init__(self, name: str, ext: str, contents: str) -> None:
        super().__init__(name, ext, "", contents)


class TS_File(File):
    def __init__(self, name: str, folder: str, contents: str) -> None:
        super().__init__(name, "ts", folder, contents)


class Empty_File(File):
    def __init__(self, name: str, ext: str, folder: str) -> None:
        super().__init__(name, ext, folder, "")


class Empty_File_Current_Dir(Empty_File):
    def __init__(self, name: str, ext: str) -> None:
        super().__init__(name, ext, "")


class HTML_File(File_In_Current_Dir):
    ext = "html"

    def __init__(self, name: str, contents: str) -> None:
        super().__init__(name, HTML_File.ext, contents)


class CSS_File(File_In_Current_Dir):
    ext = "css"

    def __init__(self, name: str, contents: str) -> None:
        super().__init__(name, CSS_File.ext, contents)


class Index_HTML_File(HTML_File):
    def __init__(self, contents: str) -> None:
        super().__init__("index", contents)


class Styles_CSS_File(CSS_File):
    def __init__(self, contents: str) -> None:
        super().__init__("styles", contents)


# ll = Index_HTML_File("asdasd")
# ll.info()


# class Empty_HTML_Current_Dir(Empty_File_Current_Dir, HTML_File):
#     def __init__(self, name: str) -> None:
#         super().__init__(name, HTML_File.ext)


# jj = Empty_HTML_Current_Dir("index")

# jj.info()


class Util_Function(TS_File):
    def __init__(self, name: str, contents: str) -> None:
        super().__init__(name, "src/utils/", contents)


class Custom_Hook(TS_File):
    def __init__(self, name: str, contents: str) -> None:
        super().__init__(name, "src/hooks/", contents)


class Logger_Hook(TS_File):
    def __init__(self, name: str, contents: str) -> None:
        super().__init__(name, "src/hooks/logger/", contents)


class TSX_File(File):
    def __init__(self, name: str, folder: str, contents: str) -> None:
        super().__init__(name, "tsx", folder, contents)


class React_Component_In_SRC_Folder(TSX_File):
    def __init__(self, name: str, contents: str) -> None:
        super().__init__(name, "src/", contents)
