import { configureStore } from "@reduxjs/toolkit";
import participants from "./participants";
import rewards from "./rewards";

const store = configureStore({
  reducer: {
    participants,
    rewards,
  },
});

export default store;
