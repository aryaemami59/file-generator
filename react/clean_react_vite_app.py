clean_react_vite_app = """import type { FC } from "react";
import { memo } from "react";
import "./App.css";

const App: FC = () => (
  <div className="App">
    <div>My App</div>
  </div>
);

export default memo(App);
"""
