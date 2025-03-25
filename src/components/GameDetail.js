import React from "react";
import { useParams, Link } from "react-router-dom";
import gameData from "../data/games.json";

const GameDetail = () => {
  const { id } = useParams();
  const game = gameData.games[id];

  if (!game) {
    return <h2>Game not found</h2>;
  }

  const locationInfo = gameData.locations[game.location];

  return (
    <div className="container mt-4">
      <h2>Game Details</h2>
      <p><strong>Date:</strong> {game.date}</p>
      <p><strong>Time:</strong> {game.time}</p>
      <p><strong>Teams:</strong> {game.teams}</p>
      <p><strong>Location:</strong> {locationInfo?.name || game.location}</p>
      <p><strong>Address:</strong> {locationInfo?.address || "Unknown"}</p>

      {locationInfo?.map && (
        <div className="map-container" style={{ marginTop: "20px" }}>
          <iframe
            title="Game Location"
            width="100%"
            height="300"
            src={locationInfo.map}
            allowFullScreen=""
            loading="lazy"
            style={{ border: "0" }}
          ></iframe>
        </div>
      )}

      <br />
      <Link to="/games" className="btn btn-primary mt-3">Back to Schedule</Link>
    </div>
  );
};

export default GameDetail;



