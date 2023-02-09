useMounted = {
    "useMounted": """import type { FC } from "react";
import { useDebugValue, useEffect } from "react";
import type { AnyObject, EmptyObject } from "../types/missingTypes";

/**
 * Checks when component mounts and unmounts
 * @param component Component that we are checking mount and unmount status for
 */

const useMounted = <P extends AnyObject = EmptyObject>(component: FC<P>) => {
  const { name } = component;
  useDebugValue(name, e => e);

  useEffect(() => {
    console.log(`%c${name}%c Mounted`, "color: aqua; font-size: 15px;", "");
    return () => {
      console.log(`%c${name}%c Unmounted`, "color: aqua; font-size: 15px;", "");
    };
  }, [name]);
};

export default useMounted;
"""
}

useDependencyChangeLogger = {
    "useDependencyChangeLogger": """import { useDebugValue, useEffect, useRef } from "react";
import type { Composite } from "../types/missingTypes";
import capitalizeFirstLetter from "../utils/capitalizeFirstLetter";

/**
 * Logs dependency changes
 * Use only in development mode
 * @param dependency The dependency that we are checking for
 * @param depName Name of the dependency that we are checking for
 */

const useDependencyChangeLogger = <T extends Composite>(
  dependency: T,
  depName = ""
) => {
  const didMount = useRef(false);
  const depType = Array.isArray(dependency)
    ? "Array"
    : capitalizeFirstLetter(typeof dependency);

  useDebugValue([depName, dependency], e => e);

  useEffect(() => {
    didMount.current = false;
    return () => {
      didMount.current = false;
    };
  }, []);

  useEffect(() => {
    if (didMount.current) {
      console.log(
        `%c${depName || "Unknown Dependency"}%c ${depType} Changed:%O`,
        "color:palegreen; font-size: 15px;",
        "",
        dependency
      );
    } else didMount.current = true;
  }, [dependency, depName, depType]);
};

export default useDependencyChangeLogger;
"""
}

useCountRender = {
    "useCountRender": """import type { FC } from "react";
import { useDebugValue, useEffect, useRef } from "react";
import type { AnyObject, EmptyObject } from "../types/missingTypes";

/**
 * Counts how many times the component re-renders
 * @param component The component that we are checking re-renders for
 */

const useCountRender = <P extends AnyObject = EmptyObject>(
  component: FC<P>
) => {
  const { name } = component;
  const ref = useRef(0);
  const didMount = useRef(false);

  useDebugValue([name, ref.current], e => e);

  useEffect(() => {
    didMount.current = false;
    ref.current = 0;
    return () => {
      didMount.current = false;
    };
  }, []);

  useEffect(() => {
    if (didMount.current) {
      ref.current += 1;
      console.log(
        `%c${name}%c Re-rendered %c${ref.current}%c ${
          ref.current === 1 ? "time" : "times"
        }`,
        "color: violet; font-size: 15px;",
        "",
        "color: violet; font-size: 15px;",
        ""
      );
    } else didMount.current = true;
  });
};

export default useCountRender;
"""
}
