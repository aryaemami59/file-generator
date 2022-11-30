useComponentStatus = {
    "useComponentStatus": """import { useEffect } from "react";

const useComponentStatus = (component: string) => {
  useEffect(() => {
    console.log(`${component} Mounted`);
    return () => {
      console.log(`${component} Unmounted`);
    };
  }, [component]);
};

export default useComponentStatus;
"""
}

useValueUpdateLogger = {
    "useValueUpdateLogger": """import { useEffect } from "react";
import type { AnyObject } from "../types/missingTypes";

const useValueUpdateLogger = (value: AnyObject | unknown[]) => {
  useEffect(() => {
    console.log(value, "changed");
  }, [value]);
};

export default useValueUpdateLogger;
"""
}
