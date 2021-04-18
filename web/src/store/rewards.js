import { createSelector } from "reselect";
import { createSlice } from "@reduxjs/toolkit";
import { uploadFile } from "./katsu";

const root = (state) => state.rewards;
export const getRootList = createSelector(root, (state) => state.list);
export const getRewards = createSelector(getRootList, (state) => state.data);

const initialState = {
  list: {
    data: [],
    loading: false,
  },
};

const redux = createSlice({
  name: "rewards",
  initialState,
  reducers: {
    inserOne(state, { payload }) {
      state.list.push(payload);
    },
    deleteOne(state, { payload }) {
      const idx = state.list.findIndex((item) => item.id === payload);
      state.list.splice(idx, 1);
    },
    updateOne(state, { payload }) {
      const idx = state.list.findIndex((item) => item.id === payload.id);
      state.list.splice(idx, 0, payload);
    },
  },
  extraReducers: {
    [uploadFile.fulfilled]: (state, { payload }) => {
      const { data } = payload;
      const { rewards } = data || {};
      state.list.data = rewards;
    },
  },
});

export const { inserOne, deleteOne, updateOne } = redux.actions;
export default redux.reducer;
