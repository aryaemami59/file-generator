import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from ts_config import ts_config
from create_files_script_ts import index_ts

ts_config_node = ts_config

ts_config_node.contents["ts-node"] = {
    "esm": True,
    "transpileOnly": True,
    "experimentalSpecifierResolution": "node",
}

files = (index_ts, ts_config_node)

if __name__ == "__main__":
    for v in files:
        v.create_file()
