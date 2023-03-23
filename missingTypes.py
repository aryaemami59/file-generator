import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from create_file import TS_File

missingTypes = TS_File(
    "missingTypes",
    "src/types/",
    """export type AnyObject = Record<string, unknown>;

export type AnyArray = unknown[];

export type AnyFunction = (...args: unknown[]) => unknown;

export type EmptyObject = Record<string, never>;

export type EmptyArray = readonly [];

export type Without<T, U> = { [P in Exclude<keyof T, keyof U>]?: never };
export type XOR<T, U> = T | U extends object
  ? (Without<T, U> & U) | (Without<U, T> & T)
  : T | U;

export type Composite = AnyFunction | AnyArray | AnyObject;

export type ObjectOrArray = AnyArray | AnyObject;

export type Equals<X, Y> = (<T>() => T extends X ? 1 : 2) extends <
  T
>() => T extends Y ? 1 : 2
  ? true
  : false;
""",
)
