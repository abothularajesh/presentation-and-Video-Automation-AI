import React from "react";

function Layout({ children }) {

  return (
    <div
      style={{
        minHeight: "100vh",
        background: "linear-gradient(135deg,#020617,#0f172a,#020617)",
        color: "white"
      }}
    >
      {children}
    </div>
  );
}

export default Layout;