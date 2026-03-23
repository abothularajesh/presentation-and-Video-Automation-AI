import React, { useState } from "react";
import { generateSlides } from "../../services/api";
import DownloadSection from "../download/DownloadSection";
import send from "../../images/send.png";

function GenerateForm() {

  const [topic, setTopic] = useState("");
  const [slides, setSlides] = useState(5);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {

    if (!topic) return;

    const token = localStorage.getItem("token");

    setLoading(true);

    try {
      const res = await generateSlides(topic, slides, token);
      setResult(res);
    } catch (e) {
      console.error(e);
    }

    setLoading(false);
  };

  return (

    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        marginTop: "100px"
      }}
    >

      {/* Main Card */}

      <div
        style={{
          width: "850px",
          maxWidth: "92%",
          background: "rgba(30,41,59,0.6)",
          padding: "40px",
          borderRadius: "20px",
          backdropFilter: "blur(12px)",
          boxShadow: "0 25px 60px rgba(0,0,0,0.5)"
        }}
      >

        <h2 style={{ marginBottom: "25px", color: "white" }}>
          Generate AI Presentation
        </h2>

        {/* Topic input */}

        <div style={{ display: "flex", alignItems: "center" }}>

          <input
            placeholder="Enter topic..."
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            style={{
              width: "100%",
              padding: "18px",
              borderRadius: "14px",
              border: "none",
              outline: "none",
              fontSize: "17px",
              background: "#0f172a",
              color: "white"
            }}
          />

          <button
            onClick={handleGenerate}
            style={{
              marginLeft: "15px",
              padding: "15px 22px",
              borderRadius: "14px",
              border: "none",
              background: "linear-gradient(135deg,#7c3aed,#a855f7)",
              color: "white",
              fontSize: "16px",
              cursor: "pointer"
            }}
          >
            <img src={send} alt="Send" width={18} />
          </button>

        </div>

        {/* Slides count */}

        <div style={{ marginTop: "25px" }}>
          <input
            type="number"
            value={slides}
            onChange={(e) => setSlides(e.target.value)}
            style={{
              padding: "12px",
              borderRadius: "10px",
              border: "none",
              width: "150px",
              background: "#0b142c",
              color: "white",
              fontSize: "15px"
            }}
          />
        </div>

      </div>

      {/* Loading Animation */}

      {loading && (
        <div style={{ marginTop: "40px", textAlign: "center" }}>

          <p style={{ marginBottom: "12px", fontWeight: "600", letterSpacing: "1px" }}>
            LOADING ....
          </p>

          <div style={{
            width: "260px",
            height: "20px",
            border: "3px solid #1e293b",
            borderRadius: "12px",
            overflow: "hidden",
            margin: "0 auto"
          }}>

            <div style={{
              height: "100%",
              width: "40%",
              background: "linear-gradient(90deg,#7c3aed,#a855f7)",
              animation: "loadingMove 1s linear infinite"
            }} />

          </div>

        </div>
      )}

      {result && <DownloadSection data={result} />}

    </div>
  );
}

export default GenerateForm;
