from eslint.eslint_react_ts import eslint_react_ts

eslint_react_native_ts = eslint_react_ts
eslint_react_native_ts["env"]["react-native/react-native"] = True
eslint_react_native_ts["extends"].insert(0, "@react-native-community")
eslint_react_native_ts["extends"].append("plugin:react-native/all")
eslint_react_native_ts["plugins"].insert(1, "react-native")
eslint_react_native_ts["rules"]["react-native/no-color-literals"] = [0]
eslint_react_native_ts["rules"]["react-native/sort-styles"] = [0]

eslintignore_react_native = "node_modules\nexpo\n.expo-shared\n.vscode\nbabel.config.js"
