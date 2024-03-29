import sys
import path


folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from my_types.my_types import ESLINT_TYPE

from create_file import ESLINT_RC_JSON, ESLINT_Ignore


def create_eslint(eslint: ESLINT_TYPE) -> None:
    ESLINT_RC_JSON(eslint).create_file()
