import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from create_folder import create_folder
from write_to_all_files import write_to_all_files
from settings import settings

capitalizeFirstLetter = """/**
 * Takes a string and returns the same string with the first letter capitalized
 * @param str String whose first letter is going to be capitalized
 */

const capitalizeFirstLetter = (str: string): string =>
  str.charAt(0).toUpperCase() + str.slice(1);

export default capitalizeFirstLetter;
"""


def create_settings() -> None:
    create_folder([".vscode"])
    write_to_all_files([(".vscode/settings.json", settings)])
    write_to_all_files([("src/utils/capitalizeFirstLetter.ts", capitalizeFirstLetter)])


if __name__ == "__main__":
    create_settings()
