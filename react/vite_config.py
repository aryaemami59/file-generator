import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from create_file import TS_File

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

# vite_config = (
#     "vite.config.ts",
#     """import react from "@vitejs/plugin-react";
# import { defineConfig } from "vite";

# // https://vitejs.dev/config/
# export default defineConfig({
#   server: {
#     port: 3000,
#     open: "http://localhost:3000/",
#   },
#   plugins: [react()],
# });
# """,
# )
