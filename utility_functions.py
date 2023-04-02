from create_file import Util_Function


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

objectKeys = Util_Function(
    "objectKeys",
    """import type { AnyObject } from "../types/missingTypes";

/**
 * A typescript helper function that improves upon the native `Object.keys` method.
 * @template {AnyObject} Obj Obj must be a valid object.
 * @param {Obj} obj Object whose keys are returned as an array.
 * @returns {(keyof Obj)[]}
 */
const objectKeys = <Obj extends AnyObject>(obj: Obj): (keyof Obj)[] =>
  Object.keys(obj) as (keyof Obj)[];

export default objectKeys;
""",
)

utility_functions = (capitalizeFirstLetter, objectKeys)
