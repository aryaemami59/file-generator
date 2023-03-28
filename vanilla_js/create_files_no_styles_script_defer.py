import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from empty_script_js import empty_script_js
from create_file import Index_HTML_File

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
      defer></script>
    <title>Document</title>
  </head>
  <body></body>
</html>
"""
)

files = (index_html, empty_script_js)

if __name__ == "__main__":
    for v in files:
        v.create_file()
