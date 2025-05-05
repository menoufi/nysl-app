import React, { useState } from "react";
import { useParams } from "react-router-dom";
import {
  useUserState,
  uploadPicture,
  getPictureUrl,
  savePictureData,
  useGamePictures
} from "../firebase";
import { ref as storageRef } from "firebase/storage"; 

import { getStorage } from "firebase/storage"; 
const storage = getStorage(); 

const GamePhotos = () => {
  const { id: gameId } = useParams();
  const [user] = useUserState();
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [pictures, loading, error] = useGamePictures(gameId);

  const handleUpload = async () => {
    if (!file || !user) return;
    setUploading(true);
    try {
      const fileName = `${Date.now()}-${file.name}`;
      const path = `pictures/${gameId}/${fileName}`;
      await uploadPicture(path, file);
      const fileRef = storageRef(storage, path); 
      const url = await getPictureUrl(fileRef);
      await savePictureData(gameId, {
        author: user.email,
        url
      });
      setFile(null);
    } catch (err) {
      console.error("Upload failed:", err);
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Photos for Game {gameId}</h2>

      <div className="mb-3">
        <input
          type="file"
          accept="image/*"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button
          className="btn btn-primary mt-2"
          onClick={handleUpload}
          disabled={!file || uploading}
        >
          {uploading ? "Uploading..." : "Upload Photo"}
        </button>
      </div>

      {loading && <p>Loading photos...</p>}
      {error && <p className="text-danger">Error loading photos: {error.message}</p>}

      {Array.isArray(pictures) && pictures.length > 0 ? (
        pictures
          .filter((pic) => pic.val().url)
          .sort((a, b) => a.val().timestamp - b.val().timestamp)
          .map((pic) => {
            const { author, url, timestamp } = pic.val();
            return (
              <div key={pic.key} className="mb-3">
                <img
                  src={url}
                  alt="Game Upload"
                  style={{ width: "100%", borderRadius: "8px" }}
                />
                <div className="text-muted small">
                  {author} — {new Date(timestamp).toLocaleTimeString()}
                </div>
              </div>
            );
          })
      ) : (
        !loading && <p>No photos yet.</p>
      )}
    </div>
  );
};

export default GamePhotos;






