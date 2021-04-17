import React from "react";
import { SetupForm } from "./components/form";

const Container = ({ children }) => (
  <div className="container mt-4"> {children} </div>
);

function App() {
  return (
    <Container>
      <SetupForm />
    </Container>
  );
}

export default App;
