import React from "react";
import { Link } from "react-router-dom";
import gameData from "../data/games.json";

const Schedule = () => {
  const games = gameData.games || {};

  return (
    <div className="container mt-4">
      <h2>Game Schedule</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Date</th>
            <th>Teams</th>
            <th>Location</th>
            <th>Time</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(games).map(([id, game]) => (
            <tr key={id}>
              <td>{game.date}</td>
              <td>{game.teams}</td>
              <td>{game.location}</td>
              <td>{game.time}</td>
              <td>
                <Link to={`/game/${id}`} className="btn btn-info btn-sm me-2">
                  Details
                </Link>
                <Link to={`/messages/${id}`} className="btn btn-success btn-sm me-2">
                  Chat
                </Link>
                <Link to={`/photos/${id}`} className="btn btn-secondary btn-sm">
                  Photos
                </Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Schedule;








