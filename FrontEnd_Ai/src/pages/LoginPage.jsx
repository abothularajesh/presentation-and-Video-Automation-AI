
import React from "react";
import { GoogleLogin } from "@react-oauth/google";
import "../styles/login.css";

function LoginPage(){

  const handleSuccess = (res)=>{
      localStorage.setItem("token",res.credential)
      window.location.reload()
  }

  return(
    <div className="login-container">
        <h1>AI Presentation Generator</h1>
        <p>Create slides instantly using AI</p>

        <GoogleLogin
          onSuccess={handleSuccess}
          onError={()=>console.log("Login failed")}
        />
    </div>
  )
}

export default LoginPage;
