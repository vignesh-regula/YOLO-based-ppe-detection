import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav style={{ padding: 15, background: "#222", color: "white" }}>
      <Link to="/" style={{ marginRight: 15, color: "white" }}>Dashboard</Link>
      <Link to="/upload" style={{ marginRight: 15, color: "white" }}>Upload</Link>
      <Link to="/login" style={{ marginRight: 15, color: "white" }}>Login</Link>
      <Link to="/register" style={{ color: "white" }}>Register</Link>
    </nav>
  );
}
