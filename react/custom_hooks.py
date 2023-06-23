from create_file import Custom_Hook, Logger_Hook

useComponentDidMount = Custom_Hook(
    "useComponentDidMount",
    """import { useEffect, useRef } from "react";

/**
 * Runs an effect when the component mounts.
 * @template {() => void} T T must be a function.
 * @param {T} callback Callback function that gets invoked when the component mounts.
 */
const useComponentDidMount = <T extends () => void>(callback: T) => {
  const callbackRef = useRef(callback);
  const memoizedCB = callbackRef.current;

  useEffect(memoizedCB, [memoizedCB]);
};

export default useComponentDidMount;
""",
)

useComponentDidUpdate = Custom_Hook(
    "useComponentDidUpdate",
    """import { useEffect, useRef } from "react";

/**
 * Runs an effect anytime the component re-renders.
 * @template {() => void} T T must be a function.
 * @param {T} callback Callback function that gets invoked anytime the component updates.
 * @param {readonly unknown[]} [deps] An optional dependency array, if provided effect will run only if the values in the list change.
 */
const useComponentDidUpdate = <T extends () => void>(
  callback: T,
  deps?: readonly unknown[]
) => {
  const didMount = useRef(false);
  const callbackRef = useRef(callback);

  useEffect(() => {
    callbackRef.current = callback;
  }, [callback]);

  useEffect(() => {
    didMount.current = false;
    return () => {
      didMount.current = false;
    };
  }, []);

  useEffect(() => {
    if (didMount.current) {
      callbackRef.current();
    } else didMount.current = true;
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps);
};

export default useComponentDidUpdate;
""",
)

useComponentWillUnmount = Custom_Hook(
    "useComponentWillUnmount",
    """import { useEffect, useRef } from "react";
/**
 * Runs an effect when the component unmounts.
 * @template {() => void} T T must be a function.
 * @param {T} callback Callback function that gets invoked when the component unmounts.
 */
const useComponentWillUnmount = <T extends () => void>(callback: T) => {
  const callbackRef = useRef(callback);
  const memoizedCB = callbackRef.current;

  useEffect(() => memoizedCB, [memoizedCB]);
};

export default useComponentWillUnmount;
""",
)

useFetch = Custom_Hook(
    "useFetch",
    """import { useCallback, useEffect, useState } from "react";
import type { ObjectOrArray } from "../types/missingTypes";

export type FetchedState<T extends ObjectOrArray> = {
  data: T;
  error: string | null;
  isLoading: boolean;
};

/**
 * `useFetch` Accepts a url as a parameter and returns an object containing the fetched data, an error state, an a loading state.
 * @template {ObjectOrArray} T The type of data we are getting back. It must be either an object or an array.
 * @param {string} url The url to fetch data from.
 * @param {RequestInit} init An optional init object that allows you to control a number of different settings.
 * @returns {FetchedState<T>} An object containing the fetched data, an error state, and a loading state.
 */
const useFetch = <T extends ObjectOrArray>(
  url: string,
  init?: RequestInit
): FetchedState<T> => {
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [data, setData] = useState<T>({} as T);

  const fetchData = useCallback(async () => {
    try {
      const response = await fetch(url, init).catch((fetchError: TypeError) => {
        throw new Error(fetchError.message);
      });
      if (!response.ok) {
        const errorMessage = `Response failed status code: ${response.status}`;
        setIsLoading(false);
        setError(errorMessage);
        throw new Error(errorMessage);
      }
      const responseData = (await response.json()) as T;
      setIsLoading(false);
      setData(responseData);
    } catch (err) {
      setIsLoading(false);
      if (err instanceof Error) {
        setError(err.message);
      }
      console.error(err);
    }
  }, [init, url]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  return { data, error, isLoading };
};

export default useFetch;
""",
)

usePreviousState = Custom_Hook(
    "usePreviousState",
    """import { useRef } from "react";

/**
 * `usePreviousState` Accepts a state value as a parameter and returns the previous state value.
 * @template {NonNullable<unknown>} T T can be any non-nullish value.
 * @param {T} state The state whose previous value is to be returned.
 * @returns {T | undefined} The previous state is returned.
 */
const usePreviousState = <T extends NonNullable<unknown>>(
  state: T
): T | undefined => {
  const currentRef = useRef<T>(state);
  const previousRef = useRef<T>();

  if (currentRef.current !== state) {
    previousRef.current = currentRef.current;
    currentRef.current = state;
  }

  return previousRef.current;
};

export default usePreviousState;
""",
)

useComponentMountLogger = Logger_Hook(
    "useComponentMountLogger",
    """import { useDebugValue, useEffect } from "react";

/**
 * Use only in development mode
 *
 * Checks when component mounts and unmounts and logs the results to the console.
 */
const useComponentMountLogger = () => {
  const componentName =
    new Error().stack?.split("\\n")[2].split(" ")[5] ?? "Component";

  useDebugValue(componentName, e => e);

  useEffect(() => {
    console.log(
      `%c${componentName}%c Mounted`,
      "color: aqua; font-size: 15px;",
      ""
    );
    return () => {
      console.log(
        `%c${componentName}%c Unmounted`,
        "color: aqua; font-size: 15px;",
        ""
      );
    };
  }, [componentName]);
};

export default useComponentMountLogger;
""",
)

useComponentUpdateLogger = Logger_Hook(
    "useComponentUpdateLogger",
    """import { useDebugValue, useRef } from "react";
import useComponentDidUpdate from "../useComponentDidUpdate";

/**
 * Use only in development mode
 *
 * Counts how many times the component re-renders and logs the results to the console.
 */
const useComponentUpdateLogger = () => {
  const componentName =
    new Error().stack?.split("\\n")[2].split(" ")[5] ?? "Component";
  const renderCount = useRef(0);

  useDebugValue([componentName, renderCount.current], e => e);

  useComponentDidUpdate(() => {
    renderCount.current += 1;
    console.log(
      `%c${componentName}%c Re-rendered %c${renderCount.current}%c ${
        renderCount.current === 1 ? "time" : "times"
      }`,
      "color: violet; font-size: 15px;",
      "",
      "color: violet; font-size: 15px;",
      ""
    );
  });
};

export default useComponentUpdateLogger;
""",
)


useDependencyChangeLogger = Logger_Hook(
    "useDependencyChangeLogger",
    """import { useDebugValue } from "react";
import capitalizeFirstLetter from "../../utils/capitalizeFirstLetter";
import useComponentDidUpdate from "../useComponentDidUpdate";

/**
 * Use only in development mode
 *
 * Checks when a single dependency changes and logs the results to the console.
 * @param dependency The dependency that we are checking for.
 * @param depName Name of the dependency that we are checking for.
 */
const useDependencyChangeLogger = <T>(dependency: T, depName = "") => {
  const componentName =
    new Error().stack?.split("\\n")[2].split(" ")[5] ?? "Component";
  const depType = Array.isArray(dependency)
    ? "Array"
    : capitalizeFirstLetter(typeof dependency);

  useDebugValue([depName, dependency], e => e);

  useComponentDidUpdate(() => {
    console.log(
      `%c${
        depName || "Unknown Dependency"
      }%c ${depType} in ${componentName} Changed: %O`,
      "color:palegreen; font-size: 15px;",
      "",
      dependency
    );
  }, [depName, depType, dependency]);
};

export default useDependencyChangeLogger;
""",
)

custom_hooks = (
    useComponentDidMount,
    useComponentDidUpdate,
    useComponentWillUnmount,
    useFetch,
    usePreviousState,
)

logger_hooks = (
    useComponentMountLogger,
    useComponentUpdateLogger,
    useDependencyChangeLogger,
)
