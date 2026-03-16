import React from "react";

function Navbar() {

  const logout = () => {
    localStorage.removeItem("token");
    window.location.reload();
  };

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        padding: "16px 40px",
        background: "linear-gradient(90deg,#0f172a,#020617)",
        color: "white"
      }}
    >
      {/* Left logo */}
      <h2 style={{color:"#8b5cf6"}}>LearnLift AI</h2>

      {/* Center menu */}
      <div style={{display:"flex",gap:"30px"}}>
        <span style={{cursor:"pointer"}}>AI Video Tutor</span>
        <span style={{cursor:"pointer"}}>Presentation Maker</span>
      </div>

      {/* Right buttons */}
      <div style={{display:"flex",gap:"15px"}}>
        <button
          style={{
            background:"#1e293b",
            color:"white",
            border:"none",
            padding:"8px 14px",
            borderRadius:"8px",
            cursor:"pointer"
          }}
        >
          ☀ Light
        </button>

        <button
          onClick={logout}
          style={{
            background:"#ef4444",
            border:"none",
            padding:"8px 14px",
            borderRadius:"8px",
            color:"white",
            cursor:"pointer"
          }}
        >
          Logout
        </button>
      </div>
    </div>
  );
}

export default Navbar;