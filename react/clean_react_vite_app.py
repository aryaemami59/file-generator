import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from create_file import React_Component_In_SRC_Folder

clean_react_vite_app = React_Component_In_SRC_Folder(
    "App",
    """import type { FC } from "react";
import { memo } from "react";
import "./App.css";

const App: FC = () => (
  <div className="App">
    <div>My App</div>
  </div>
);

export default memo(App);
""",
)
