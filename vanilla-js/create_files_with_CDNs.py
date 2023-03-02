import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from styles_css import styles_css
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
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa"
      crossorigin="anonymous"
      defer></script>
    <script
      src="https://code.jquery.com/jquery-3.6.0.min.js"
      integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
      crossorigin="anonymous"
      defer></script>
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css"
      integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx"
      crossorigin="anonymous" />
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
"""
)

files = (index_html, styles_css, empty_script_js)


if __name__ == "__main__":
    for v in files:
        v.create_file()
