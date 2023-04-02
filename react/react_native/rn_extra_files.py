import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent.parent)
from create_file import TS_File, File_In_Current_Dir, TS_CONFIG_JSON


index_d_ts = TS_File(
    "index.d",
    "src/types/",
    """declare module "ts-node/register" {}
""",
)

webpack_ts = TS_File(
    "webpack.config",
    "",
    """import createExpoWebpackConfigAsync from "@expo/webpack-config/webpack";
import type {
  Arguments,
  Environment,
} from "@expo/webpack-config/webpack/types";

module.exports = async (env: Environment, argv: Arguments) => {
  const config = await createExpoWebpackConfigAsync(env, argv);
  // Customize the config before returning it.
  return config;
};
""",
)

webpack_js = File_In_Current_Dir(
    "webpack.config",
    "js",
    """require("ts-node/register");
module.exports = require("./webpack.config.ts");
""",
)

rn_ts_config = TS_CONFIG_JSON(
    {
        "extends": "expo/tsconfig.base",
        "compilerOptions": {
            "strict": True,
            "noImplicitAny": True,
            "forceConsistentCasingInFileNames": True,
        },
        "include": ["**/*"],
        "files": ["./webpack.config.js"],
    },
)

babel_config = File_In_Current_Dir(
    "babel.config",
    "js",
    """/** @type {import('@babel/core').ConfigFunction} */
module.exports = api => {
  api.cache.forever();
  return {
    presets: ["babel-preset-expo"],
  };
};
""",
)

rn_extra_files = (
    index_d_ts,
    webpack_ts,
    webpack_js,
    rn_ts_config,
    babel_config,
)
