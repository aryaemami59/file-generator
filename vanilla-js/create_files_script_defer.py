import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from write_to_all_files import write_to_all_files
from styles_css import styles_css
from empty_script_js import empty_script_js

index_html = (
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


if __name__ == "__main__":
    write_to_all_files([index_html, styles_css, empty_script_js])
