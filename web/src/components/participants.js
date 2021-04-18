import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { updateOne } from "../store/participants";

import { getParticipants } from "../store/participants";

const Participant = ({ data }) => {
  const dispatch = useDispatch();
  const [edit, setEdit] = useState(false);
  const [name, setName] = useState(`${data.name} ${data?.lastname} `);

  const handler = () => {
    setEdit(!edit);
    dispatch(updateOne({ ...data, name }));
  };
  const handleChange = (event) => setName(event.target.value);
  if (edit) {
    return (
      <input
        type="text"
        name="name"
        value={name}
        onChange={handleChange}
        onBlur={handler}
      />
    );
  }
  return <div onDoubleClick={handler}>{name}</div>;
};

const Participants = () => {
  const items = useSelector(getParticipants);
  return (
    <div className="">
      {items.map((item) => (
        <div key={item.id}>
          <Participant data={item} />
        </div>
      ))}
    </div>
  );
};

export default Participants;
