from write_to_all_files import write_to_all_files
from create_file import Util_Function

# utility_functions = {
#     "capitalizeFirstLetter": """/**
#  * Takes a string and returns the same string with the first letter capitalized
#  * @param str String whose first letter is going to be capitalized
#  */

# const capitalizeFirstLetter = (str: string): string =>
#   str.charAt(0).toUpperCase() + str.slice(1);

# export default capitalizeFirstLetter;
#     """
# }


# class File:
#     def __init__(self, name: str, ext: str, folder: str, contents: str) -> None:
#         self.name = name
#         self.contents = contents
#         self.ext = ext
#         self.folder = folder
#         self.directory = f"{folder}{name}.{ext}"

#     def create_file(self) -> None:
#         write_to_all_files([(self.directory, self.contents)])


# class Util_Function(File):
#     def __init__(self, name: str, folder: str, contents: str) -> None:
#         self.ext = "ts"
#         super().__init__(name, self.ext, folder, contents)


# class TSX_File(File):
#     def __init__(self, name: str, folder: str, contents: str) -> None:
#         self.ext = "tsx"
#         super().__init__(name, self.ext, folder, contents)


capitalizeFirstLetter = Util_Function(
    "capitalizeFirstLetter",
    """/**
 * Takes a string and returns the same string with the first letter capitalized
 * @param str String whose first letter is going to be capitalized
 */

const capitalizeFirstLetter = (str: string): string =>
  str.charAt(0).toUpperCase() + str.slice(1);

export default capitalizeFirstLetter;
    """,
)

utility_functions = (capitalizeFirstLetter,)

# capitalizeFirstLetter.create_file()


# def create_files(files_dict: dict[str, str]) -> None:
#     write_to_all_files([(k, v) for k, v in files_dict.items()])
