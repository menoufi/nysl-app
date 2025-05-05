import React, { useState } from "react";
import { useParams } from "react-router-dom";
import { useUserState, useGameMessages, addMessage } from "../firebase";

const Messages = () => {
  const { id: gameId } = useParams();
  const [user] = useUserState();
  const [text, setText] = useState("");
  const [messages, loading, error] = useGameMessages(gameId);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!text.trim() || !user) return;

    await addMessage(gameId, {
      author: user.email,
      text,
    });

    setText("");
  };

  const filteredMessages = messages
    ? messages.filter((msg) => msg.val().timestamp).sort((a, b) => a.val().timestamp - b.val().timestamp)
    : [];

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Message Board</h2>

      <div className="mb-3 overflow-auto" style={{ maxHeight: "400px" }}>
        {loading && <p>Loading messages...</p>}
        {error && <p>Error: {error.message}</p>}
        {filteredMessages.length > 0 ? (
          filteredMessages.map((msg) => {
            const { author, text, timestamp } = msg.val();
            const time = new Date(timestamp).toLocaleTimeString();
            return (
              <div key={msg.key} className="border rounded p-2 mb-2 bg-light">
                <small className="text-muted">{author} — {time}</small>
                <p className="mb-0">{text}</p>
              </div>
            );
          })
        ) : (
          <p>No messages yet.</p>
        )}
      </div>

      {user ? (
        <form onSubmit={handleSubmit} className="mt-3">
          <div className="input-group">
            <input
              type="text"
              className="form-control"
              placeholder="Type your message..."
              value={text}
              onChange={(e) => setText(e.target.value)}
            />
            <button className="btn btn-primary" type="submit">
              Send
            </button>
          </div>
        </form>
      ) : (
        <p className="text-muted">You must be signed in to post messages.</p>
      )}
    </div>
  );
};

export default Messages;






  