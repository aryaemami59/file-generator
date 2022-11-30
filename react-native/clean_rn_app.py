clean_rn_app = """import { StatusBar } from "expo-status-bar";
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
"""
