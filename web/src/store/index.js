import { configureStore } from "@reduxjs/toolkit";
import participants from "./participants";
import rewards from "./rewards";
import katsu from "./katsu";

const store = configureStore({
  reducer: {
    participants,
    rewards,
    katsu,
  },
});

export default store;
