import React, { useState } from "react";

export default function UploadPPE() {
  const [video1, setVideo1] = useState(null);
  const [video2, setVideo2] = useState(null);
  const [loading, setLoading] = useState(false);

  const uploadVideos = async (e) => {
    e.preventDefault();
    setLoading(true);
    setVideo1(null);
    setVideo2(null);

    try {
      const formData = new FormData(e.target);

      const res = await fetch("http://localhost:5000/upload", {
        method: "POST",
        body: formData,
      });

      if (!res.ok) {
        throw new Error("Upload failed");
      }

      const data = await res.json();

      if (data.video1) {
        setVideo1(`http://localhost:5000/stream/${data.video1}`);
      }

      if (data.video2) {
        setVideo2(`http://localhost:5000/stream/${data.video2}`);
      }

    } catch (err) {
      alert("Error uploading videos: " + err.message);
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 1100, margin: "30px auto", fontFamily: "sans-serif" }}>
      <h2>Upload Videos for Real-Time PPE Detection</h2>

      <form onSubmit={uploadVideos}>
        <div style={{ marginBottom: 10 }}>
          <label>Video 1: </label>
          <input type="file" name="video1" accept="video/*" />
        </div>

        <div style={{ marginBottom: 10 }}>
          <label>Video 2: </label>
          <input type="file" name="video2" accept="video/*" />
        </div>

        <button type="submit">Upload & Start Detection</button>
      </form>

      {loading && <p>Processing videos...</p>}

      <div style={{ display: "flex", gap: "20px", marginTop: "20px" }}>
        {video1 && (
          <div>
            <h3>Stream 1</h3>
            <img
              src={video1}
              alt="Video Stream 1"
              style={{ width: "500px", border: "2px solid #00ff00" }}
            />
          </div>
        )}

        {video2 && (
          <div>
            <h3>Stream 2</h3>
            <img
              src={video2}
              alt="Video Stream 2"
              style={{ width: "500px", border: "2px solid #00ff00" }}
            />
          </div>
        )}
      </div>
    </div>
  );
}
