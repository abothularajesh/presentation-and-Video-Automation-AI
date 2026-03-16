import React from "react";

function DownloadSection({ data }) {

  const downloadPPT = () => {
    window.open("http://localhost:8000" + data.ppt);
  };

  const downloadVideo = () => {
    if(data.video){
      window.open("http://localhost:8000" + data.video);
    }
  };

  return(

    <div style={{
      marginTop:"40px",
      display:"flex",
      gap:"20px",
      justifyContent:"center"
    }}>

      <button
        onClick={downloadPPT}
        style={{
          padding:"12px 20px",
          borderRadius:"10px",
          border:"none",
          background:"#22c55e",
          color:"white",
          cursor:"pointer"
        }}
      >
        Download PPT
      </button>

      <button
        onClick={downloadVideo}
        style={{
          padding:"12px 20px",
          borderRadius:"10px",
          border:"none",
          background:"#6366f1",
          color:"white",
          cursor:"pointer"
        }}
      >
        Download Video
      </button>

    </div>
  );
}

export default DownloadSection;