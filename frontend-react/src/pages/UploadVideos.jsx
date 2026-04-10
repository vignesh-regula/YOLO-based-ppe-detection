import React, { useState } from "react";

export default function UploadVideos() {
  const [video1, setVideo1] = useState(null);
  const [video2, setVideo2] = useState(null);
  const [loading, setLoading] = useState(false);

  const uploadVideos = async (e) => {
    e.preventDefault();
    setLoading(true);

    const formData = new FormData(e.target);

    const res = await fetch("http://localhost:5000/upload", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();

    if (data.video1)
      setVideo1(`http://localhost:5000/stream/${data.video1}`);

    if (data.video2)
      setVideo2(`http://localhost:5000/stream/${data.video2}`);

    setLoading(false);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Upload Videos</h2>

      <form onSubmit={uploadVideos}>
        <input type="file" name="video1" accept="video/*" />
        <input type="file" name="video2" accept="video/*" />
        <button type="submit">Upload</button>
      </form>

      {loading && <p>Processing...</p>}

      <div style={{ display: "flex", gap: 20, marginTop: 20 }}>
        {video1 && <img src={video1} width="500" />}
        {video2 && <img src={video2} width="500" />}
      </div>
    </div>
  );
}
