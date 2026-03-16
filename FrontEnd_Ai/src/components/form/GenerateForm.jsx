import React,{useState} from "react";
import { generateSlides } from "../../services/api";
import DownloadSection from "../download/DownloadSection";
import send from "../../images/send.png";

function GenerateForm(){

  const [topic,setTopic] = useState("");
  const [slides,setSlides] = useState(5);
  const [result,setResult] = useState(null);
  const [loading,setLoading] = useState(false);

  const handleGenerate = async()=>{

    if(!topic) return;

    const token = localStorage.getItem("token");

    setLoading(true);

    try{
      const res = await generateSlides(topic,slides,token);
      setResult(res);
    }catch(e){
      console.error(e);
    }

    setLoading(false);
  };

  return(

    <div style={{
      display:"flex",
      flexDirection:"column",
      alignItems:"center",
      marginTop:"80px"
    }}>

      {/* Main Search Card */}

      <div style={{
        width:"700px",
        background:"rgba(30,41,59,0.6)",
        padding:"30px",
        borderRadius:"18px",
        backdropFilter:"blur(10px)",
        boxShadow:"0 20px 50px rgba(0,0,0,0.4)"
      }}>

        <input
          placeholder="Enter topic..."
          value={topic}
          onChange={(e)=>setTopic(e.target.value)}
          style={{
            width:"80%",
            padding:"16px",
            borderRadius:"12px",
            border:"none",
            outline:"none",
            fontSize:"16px",
            background:"#0f172a",
            color:"white"
          }}
        />

        <button
          onClick={handleGenerate}
          style={{
            marginLeft:"15px",
            padding:"14px 20px",
            borderRadius:"12px",
            border:"none",
            background:"linear-gradient(135deg,#7c3aed,#a855f7)",
            color:"white",
            fontSize:"16px",
            cursor:"pointer"
          }}
        >
        <img src={send} alt="Send" width={17} />
        </button>

        <div style={{marginTop:"20px"}}>
          <input
            type="number"
            value={slides}
            onChange={(e)=>setSlides(e.target.value)}
            style={{
              padding:"10px",
              borderRadius:"8px",
              border:"none",
              width:"120px"
            }}
          />
        </div>

      </div>

      {loading && (
        <p style={{marginTop:"20px"}}>
          Generating presentation...
        </p>
      )}

      {result && <DownloadSection data={result}/>}

    </div>

  );
}

export default GenerateForm;