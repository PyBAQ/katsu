import { createSelector } from "reselect";
import { createSlice } from "@reduxjs/toolkit";
import { uploadFile } from "./katsu";

const root = (state) => state.participants;
export const getRootList = createSelector(root, (state) => state.list);
export const getParticipants = createSelector(
  getRootList,
  (state) => state.data
);

const initialState = {
  list: {
    data: [],
    loading: false,
  },
};

const redux = createSlice({
  name: "participants",
  initialState,
  reducers: {
    inserOne(state, { payload }) {
      state.list.data.push(payload);
    },
    deleteOne(state, { payload }) {
      const idx = state.list.data.findIndex((item) => item.id === payload);
      state.list.data.splice(idx, 1);
    },
    updateOne(state, { payload }) {
      const idx = state.list.data.findIndex((item) => item.id === payload.id);
      state.list.data.splice(idx, 1, payload);
    },
  },
  extraReducers: {
    [uploadFile.fulfilled]: (state, { payload }) => {
      const { data } = payload;
      const { participants } = data || {};
      state.list.data = participants;
    },
  },
});

export const { inserOne, deleteOne, updateOne } = redux.actions;
export default redux.reducer;
