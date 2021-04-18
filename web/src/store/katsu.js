import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import http from "../helpers/http";

export const uploadFile = createAsyncThunk(
  "katsu/uploadFile",
  async (payload, thunkAPI) => {
    const response = await http.post("upload/", payload);
    return response.data;
  }
);

const redux = createSlice({
  name: "katsu",
  initialState: {},
  reducers: {},
});

export default redux.reducer;
