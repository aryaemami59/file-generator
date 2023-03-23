import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent.parent)
from create_file import React_Component_In_SRC_Folder


clean_rn_app = React_Component_In_SRC_Folder(
    "App",
    """import { StatusBar } from "expo-status-bar";
import type { FC } from "react";
import { memo } from "react";
import { Text, View } from "react-native";
import { SafeAreaProvider } from "react-native-safe-area-context";

const App: FC = () => (
  <SafeAreaProvider>
    <View>
      <Text>Open up App.tsx to start working on your app!</Text>
      <StatusBar />
    </View>
  </SafeAreaProvider>
);

export default memo(App);
""",
)
