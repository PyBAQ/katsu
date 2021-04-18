import React from "react";
import { SetupForm } from "./components/form";
import Rewards from "./components/rewards";
import Participants from "./components/participants";

const Container = ({ children }) => (
  <div className="container mt-4"> {children} </div>
);

function App() {
  return (
    <Container>
      <SetupForm />
      <div className="row">
        <div className="col">
          <Participants />
        </div>
        <div className="col">
          <Rewards />
        </div>
      </div>
    </Container>
  );
}

export default App;
