import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from ts_config import ts_config
from styles_css import styles_css
from create_file import Index_HTML_File, TS_File

index_html = Index_HTML_File(
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


script_ts = TS_File(
    "script",
    "",
    """export type AnyObject = Record<string, unknown>;

export {};
""",
)

files = (index_html, styles_css, script_ts, ts_config)


if __name__ == "__main__":
    for v in files:
        v.create_file()
