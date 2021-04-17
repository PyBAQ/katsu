import { createSlice } from "@reduxjs/toolkit";

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
});

export const { increment, decrement, incrementByAmount } = redux.actions;
export default redux.reducer;
