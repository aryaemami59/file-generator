import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from create_file import TS_File, File_In_Current_Dir, TS_CONFIG_JSON

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
            "target": "ESNext",
            "useDefineForClassFields": True,
            "lib": ["DOM", "DOM.Iterable", "ESNext"],
            "allowJs": False,
            "skipLibCheck": True,
            "esModuleInterop": False,
            "allowSyntheticDefaultImports": True,
            "strict": True,
            "forceConsistentCasingInFileNames": True,
            "module": "ESNext",
            "moduleResolution": "node",
            "resolveJsonModule": True,
            "isolatedModules": True,
            "noEmit": True,
            "jsx": "react-jsx",
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
#     "useDefineForClassFields": true,
#     "lib": ["DOM", "DOM.Iterable", "ESNext"],
#     "allowJs": false,
#     "skipLibCheck": true,
#     "esModuleInterop": false,
#     "allowSyntheticDefaultImports": true,
#     "strict": true,
#     "forceConsistentCasingInFileNames": true,
#     "module": "ESNext",
#     "moduleResolution": "Node",
#     "resolveJsonModule": true,
#     "isolatedModules": true,
#     "noEmit": true,
#     "jsx": "react-jsx",
#     "types": ["vite/client"]
#   },
#   "include": ["src"],
#   "references": [{ "path": "./tsconfig.node.json" }]
# }
# """,
# )
