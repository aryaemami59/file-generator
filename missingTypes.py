import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from create_file import TS_File

missingTypes = TS_File(
    "missingTypes",
    "src/types/",
    """export type AnyObject = Record<string, unknown>;

export type AnyArray = unknown[];

export type AnyFunction = () => unknown;

export type EmptyObject = Record<string, never>;

export type EmptyArray = [];

export type Composite = AnyFunction | AnyArray | AnyObject;
""",
)

# missingTypes = (
#     "src/types/missingTypes.ts",
#     """export type AnyObject = Record<string, unknown>;

# export type AnyArray = unknown[];

# export type AnyFunction = () => unknown;

# export type EmptyObject = Record<string, never>;

# export type EmptyArray = [];

# export type Composite = AnyFunction | AnyArray | AnyObject;
# """,
# )
