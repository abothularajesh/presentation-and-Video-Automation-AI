import React from "react";

function Layout({ children }) {

  return (
    <div
      style={{
        minHeight: "100vh",
        transition: "0.3s"
      }}
    >
      {children}
    </div>
  );
}

export default Layout;
