import sys
import path

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent.parent)
import os


from create_file import TS_File, React_Component_In_SRC_Folder, TSX_File

redux_hooks = TS_File(
    "hooks",
    "src/redux/",
    """import type { TypedUseSelectorHook } from "react-redux";
import { useDispatch, useSelector } from "react-redux";
import type { AppDispatch, RootState } from "./store";

export const useAppDispatch = () => useDispatch<AppDispatch>();
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;
""",
)

redux_store = TS_File(
    "store",
    "src/redux/",
    """import type { Action, ThunkAction } from "@reduxjs/toolkit";
import { configureStore } from "@reduxjs/toolkit";
import logger from "redux-logger";
import counterReducer from "./counterSlice";

export const store = configureStore({
  reducer: {
    counter: counterReducer,
  },
  middleware: getDefaultMiddleware =>
    process.env.NODE_ENV === "production"
      ? getDefaultMiddleware({
          thunk: true,
          serializableCheck: false,
          immutableCheck: false,
        })
      : getDefaultMiddleware({
          thunk: true,
          serializableCheck: false,
          immutableCheck: false,
        }).concat(logger),
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;
""",
)

redux_types = TS_File(
    "redux",
    "src/types/",
    """export type CounterState = {
  value: number;
  status: "idle" | "loading" | "failed";
};
""",
)

redux_slice = TS_File(
    "counterSlice",
    "src/redux/",
    """import type { PayloadAction } from "@reduxjs/toolkit";
import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import type { CounterState } from "../types/redux";

const URL = "https://randomuser.me/api";

const initialState: CounterState = {
  value: 0,
  status: "idle",
};

export const incrementAsync = createAsyncThunk(
  "counter/fetchCount",
  async () => {
    try {
      const response = await fetch(URL).catch((error: string) => {
        throw new Error(error);
      });
      if (!response.ok) {
        throw new Error(`response failed ${response.status}`);
      }
      const data = (await response.json()) as unknown[];
      return data;
    } catch (err) {
      throw new Error("Unable to fetch");
    }
  }
);

export const counterSlice = createSlice({
  name: "counter",
  initialState,
  reducers: {
    incrementByAmount: (state, action: PayloadAction<number>) => {
      state.value += action.payload;
    },
  },
  extraReducers: builder => {
    builder
      .addCase(incrementAsync.pending, state => {
        state.status = "loading";
      })
      .addCase(incrementAsync.fulfilled, (state, action) => {
        state.status = "idle";
      })
      .addCase(incrementAsync.rejected, state => {
        state.status = "failed";
      });
  },
});

export const { incrementByAmount } = counterSlice.actions;

export default counterSlice.reducer;
""",
)

redux_main = React_Component_In_SRC_Folder(
    "main",
    """import React from "react";
import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import App from "./App";
import { store } from "./redux/store";

const container = document.getElementById("root") as HTMLDivElement;
const root = createRoot(container);

root.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>
);
""",
)

redux_app = TSX_File(
    "App",
    "",
    """import { StatusBar } from "expo-status-bar";
import type { FC } from "react";
import { memo } from "react";
import { Text, View } from "react-native";
import { SafeAreaProvider } from "react-native-safe-area-context";
import { Provider } from "react-redux";
import { store } from "./src/redux/store";

const App: FC = () => (
  <Provider store={store}>
    <SafeAreaProvider>
      <View>
        <Text>Open up App.tsx to start working on your app!</Text>
        <StatusBar />
      </View>
    </SafeAreaProvider>
  </Provider>
);

export default memo(App);""",
)

redux_selectors = TS_File(
    "selectors",
    "src/redux/",
    """import type { RootState } from "./store";

export const selectCount = (state: RootState) => state.counter.value;

export const selectStatus = (state: RootState) => state.counter.status;
""",
)

# redux_ts_config = react_ts_config

# redux_ts_config.contents["compilerOptions"]["types"].append("node")

redux_files = (
    redux_hooks,
    redux_store,
    redux_types,
    redux_slice,
    # redux_main,
    redux_selectors,
    # redux_ts_config,
)


def get_redux_files():
    if os.path.isfile("src/main.tsx"):
        print("yes")
        return redux_files + (redux_main,)
    else:
        print("no")
        return redux_files + (redux_app,)
