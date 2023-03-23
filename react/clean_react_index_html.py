import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from create_file import HTML_File

clean_react_index_html = HTML_File(
    "index",
    """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0" />
    <title>Arya's Project</title>
  </head>
  <body>
    <div id="root"></div>
    <script
      type="module"
      src="/src/main.tsx"></script>
  </body>
</html>
""",
)
