import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from create_file import React_Component_In_SRC_Folder

clean_react_vite_main = React_Component_In_SRC_Folder(
    "main",
    """import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";

const container = document.getElementById("root") as HTMLDivElement;
const root = createRoot(container);

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
""",
)
