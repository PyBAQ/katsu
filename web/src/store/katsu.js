import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import http from "../helpers/http";

// First, create the thunk
export const uploadFile = createAsyncThunk(
  "katsu/uploadFile",
  async (payload, thunkAPI) => {
    const response = await http.post("upload/", payload);
    return response.data;
  }
);

// Then, handle actions in your reducers:
const katsuSlice = createSlice({
  name: "katsu",
  initialState: {},
  reducers: {},
  extraReducers: {
    [uploadFile.fulfilled]: () => {
      console.debug("here");
    },
  },
});

export default katsuSlice.reducers;
