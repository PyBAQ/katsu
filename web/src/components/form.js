import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { uploadFile } from "../store/katsu";

export const SetupForm = () => {
  const dispatch = useDispatch();
  const [participants, setParticipants] = useState("");
  const [rewards, setRewards] = useState("");
  const onchangeHandler = (data) => {
    const { files, name } = data.target;
    let file;

    if (files.length > 0) {
      file = files[0];
    }

    if (name === "participants") {
      setParticipants(file);
    }
    if (name === "rewards") {
      setRewards(file);
    }
  };

  const onSubmitHandler = (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("participants", participants, participants.name);
    formData.append("rewards", rewards, rewards.name);

    dispatch(uploadFile(formData));
  };
  return (
    <form onSubmit={onSubmitHandler}>
      <div class="row g-3 align-items-center">
        <div class="col-auto">
          <label class="col-form-label">Participantes</label>
        </div>
        <div class="col-auto">
          <input
            class="form-control"
            type="file"
            name="participants"
            accept=".csv"
            onChange={onchangeHandler}
          />
        </div>

        <div class="col-auto">
          <label class="col-form-label">Premios</label>
        </div>
        <div class="col-auto">
          <input
            class="form-control"
            type="file"
            name="rewards"
            accept=".csv"
            onChange={onchangeHandler}
          />
        </div>
      </div>

      <div className="row mt-4 d-flex justify-content-end">
        <div class="col-auto" style={{ marginRight: "26px" }}>
          <button type="submit" class="btn btn-primary">
            Submit
          </button>
        </div>
      </div>
    </form>
  );
};
