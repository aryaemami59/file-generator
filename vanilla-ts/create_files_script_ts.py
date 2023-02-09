import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from write_to_all_files import write_to_all_files
from ts_config import ts_config
from styles_css import styles_css

script_ts_html = (
    "index.html",
    """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta
      http-equiv="X-UA-Compatible"
      content="IE=edge" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0" />
    <script
      src="script.js"
      type="module"
      defer></script>
    <link
      rel="stylesheet"
      href="styles.css" />
    <title>Document</title>
  </head>
  <body></body>
</html>
""",
)


script_ts = (
    "script.ts",
    """export type AnyObject = Record<string, unknown>;

export {};
""",
)


if __name__ == "__main__":
    write_to_all_files(
        [
            script_ts_html,
            styles_css,
            ts_config,
            script_ts,
        ]
    )
