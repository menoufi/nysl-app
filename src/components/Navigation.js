import React from "react";
import { NavLink } from "react-router-dom";
import { signInWithGoogle, signOutUser, useUserState } from "../firebase";

const Navigation = () => {
  const [user] = useUserState(); 

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container">
        <NavLink className="navbar-brand" to="/">NYSL League</NavLink>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav me-auto">
            <li className="nav-item">
              <NavLink className="nav-link" to="/">Home</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/games">Schedule</NavLink>
            </li>
          </ul>
          <ul className="navbar-nav">
            {
              user ? (
                <>
                  <li className="nav-item">
                    <span className="navbar-text text-white me-3">
                      Signed in as: {user.displayName}
                    </span>
                  </li>
                  <li className="nav-item">
                    <button onClick={signOutUser} className="btn btn-outline-light btn-sm">Sign Out</button>
                  </li>
                </>
              ) : (
                <li className="nav-item">
                  <button onClick={signInWithGoogle} className="btn btn-outline-light btn-sm">Sign In</button>
                </li>
              )
            }
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;



