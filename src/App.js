import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./components/Home";
import Schedule from "./components/Schedule";
import GameDetail from "./components/GameDetail";
import Navigation from "./components/Navigation";

const App = () => {
  return (
    <Router>
      <Navigation />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/games" element={<Schedule />} />
        <Route path="/game/:id" element={<GameDetail />} />
      </Routes>
    </Router>
  );
};

export default App;








