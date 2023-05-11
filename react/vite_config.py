import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from create_file import TS_File, TS_CONFIG_JSON

vite_config = TS_File(
    "vite.config",
    "",
    """import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    port: 3000,
    open: "http://localhost:3000/",
  },
  plugins: [react()],
});
""",
)

react_ts_config = TS_CONFIG_JSON(
    {
        "compilerOptions": {
            "allowImportingTsExtensions": True,
            "isolatedModules": True,
            "jsx": "react-jsx",
            "lib": ["DOM", "DOM.Iterable", "ESNext"],
            "module": "ESNext",
            "moduleResolution": "bundler",
            "noEmit": True,
            "noFallthroughCasesInSwitch": True,
            "noUnusedLocals": True,
            "resolveJsonModule": True,
            "skipLibCheck": True,
            "strict": True,
            "target": "ESNext",
            "types": ["vite/client"],
        },
        "include": ["src"],
        "references": [{"path": "./tsconfig.node.json"}],
    },
)
# react_ts_config = File_In_Current_Dir(
#     "tsconfig",
#     "json",
#     """{
#   "compilerOptions": {
#     "target": "ESNext",
#     "useDefineForClassFields": True,
#     "lib": ["DOM", "DOM.Iterable", "ESNext"],
#     "allowJs": false,
#     "skipLibCheck": True,
#     "esModuleInterop": false,
#     "allowSyntheticDefaultImports": True,
#     "strict": True,
#     "forceConsistentCasingInFileNames": True,
#     "module": "ESNext",
#     "moduleResolution": "Node",
#     "resolveJsonModule": True,
#     "isolatedModules": True,
#     "noEmit": True,
#     "jsx": "react-jsx",
#     "types": ["vite/client"]
#   },
#   "include": ["src"],
#   "references": [{ "path": "./tsconfig.node.json" }]
# }
# """,
# )
