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
        className="form-control"
        type="text"
        name="name"
        value={name}
        onChange={handleChange}
        onBlur={handler}
      />
    );
  }
  return <div onDoubleClick={handler}>{`${data.name} ${data?.lastname} `}</div>;
};

const Participants = () => {
  const items = useSelector(getParticipants);
  return (
    <div className="">
      <ul>
        {items.map((item) => (
          <li key={item.id}>
            <Participant data={item} />
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Participants;
