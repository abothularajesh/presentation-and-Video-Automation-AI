import React from "react";

function DownloadSection({ data }) {

  const downloadPPT = () => {
    if (!data || !data.ppt) return;
    window.open(`http://localhost:8000${data.ppt}`, "_blank");
  };

  const downloadVideo = () => {
    if (!data || !data.video) return;
    window.open(`http://localhost:8000${data.video}`, "_blank");
  };

  return (

    <div
      style={{
        marginTop: "50px",
        display: "flex",
        gap: "25px",
        justifyContent: "center"
      }}
    >

      {/* PPT BUTTON */}

      <button
        onClick={downloadPPT}
        disabled={!data?.ppt}
        className="download-btn ppt-btn"
      >
        ⬇ Download PPT
      </button>

      {/* VIDEO BUTTON */}

      <button
        onClick={downloadVideo}
        disabled={!data?.video}
        className="download-btn video-btn"
      >
        ⬇ Download Video
      </button>

    </div>
  );
}

export default DownloadSection;
