import React, { useEffect, useState } from "react";

function Navbar() {

  const [darkMode, setDarkMode] = useState(true);

  const logout = () => {
    localStorage.removeItem("token");
    window.location.reload();
  };

  const toggleTheme = () => {
    const newMode = !darkMode;
    setDarkMode(newMode);

    if (newMode) {
      document.body.classList.add("dark-mode");
      localStorage.setItem("theme", "dark");
    } else {
      document.body.classList.remove("dark-mode");
      localStorage.setItem("theme", "light");
    }
  };

  useEffect(() => {
    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "light") {
      setDarkMode(false);
      document.body.classList.remove("dark-mode");
    } else {
      document.body.classList.add("dark-mode");
    }
  }, []);

  return (
    <div className="navbar"
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        padding: "18px 50px"
      }}
    >
      {/* Left logo */}
      <h2 style={{ color: "#8b5cf6", letterSpacing: "1px" }}>
        LearnLift AI
      </h2>

      {/* Center menu */}
      <div style={{ display: "flex", gap: "40px", fontSize: "15px" }}>
        <span style={{ cursor: "pointer" }}>AI Video Tutor</span>
        <span style={{ cursor: "pointer" }}>Presentation Maker</span>
      </div>

      {/* Right buttons */}
      <div style={{ display: "flex", gap: "15px" }}>

        <button
          onClick={toggleTheme}
          style={{
            background: "#26384f",
            color: "white",
            border: "none",
            padding: "9px 16px",
            borderRadius: "10px",
            cursor: "pointer",
            fontSize: "14px"
          }}
        >
          {darkMode ? "☀ Light" : "🌙 Dark"}
        </button>

        <button
          onClick={logout}
          style={{
            background: "#ae3131",
            border: "none",
            padding: "9px 16px",
            borderRadius: "10px",
            color: "white",
            cursor: "pointer",
            fontSize: "14px"
          }}
        >
          Logout
        </button>
      </div>
    </div>
  );
}

export default Navbar;
