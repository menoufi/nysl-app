import React from "react";
import { NavLink, useLocation } from "react-router-dom";
import { signInWithGoogle, signOutUser, useUserState } from "../firebase";

const Navigation = () => {
  const [user] = useUserState();
  const location = useLocation();

  const gameIdMatch = location.pathname.match(/^\/game\/(.+)$/);
  const gameId = gameIdMatch ? gameIdMatch[1] : null;

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container-fluid">
        <NavLink className="navbar-brand" to="/">NYSL League</NavLink>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNavAltMarkup"
          aria-controls="navbarNavAltMarkup"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div className="navbar-nav me-auto">
            <NavLink className="nav-link" to="/">Home</NavLink>
            <NavLink className="nav-link" to="/games">Schedule</NavLink>
            {user && gameId && (
              <NavLink className="nav-link" to={`/messages/${gameId}`}>Chat</NavLink>
            )}
          </div>
          <div className="navbar-nav">
            {user ? (
              <>
                <span className="navbar-text text-white me-3">
                  Signed in as: {user.displayName}
                </span>
                <button onClick={signOutUser} className="btn btn-outline-light btn-sm">Sign Out</button>
              </>
            ) : (
              <button onClick={signInWithGoogle} className="btn btn-outline-light btn-sm">Sign In</button>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;







