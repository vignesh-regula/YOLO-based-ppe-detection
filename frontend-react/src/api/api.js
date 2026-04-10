const BASE_URL = "http://localhost:5000";

export const uploadVideos = async (formData) => {
  const res = await fetch(`${BASE_URL}/upload`, {
    method: "POST",
    body: formData,
  });
  return res.json();
};
