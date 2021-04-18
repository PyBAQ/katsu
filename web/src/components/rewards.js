import React from "react";
import { useSelector } from "react-redux";
import { getRewards } from "../store/rewards";

const Rewards = () => {
  const items = useSelector(getRewards);
  return (
    <div className="">
      <ul>
        {items.map((item) => (
          <li key={item.id}> {item.premio} </li>
        ))}
      </ul>
    </div>
  );
};

export default Rewards;
