import React from "react";
import { GoogleLogin } from "@react-oauth/google";
import "../styles/login.css";

function LoginPage(){

const handleSuccess = (res)=>{
localStorage.setItem("token", res.credential)
window.location.reload()
}

return( <div className="login-container">

    <div className="login-card">

        <h2>Sign in</h2>
        <p className="create-account">or create an account</p>

        <input 
          type="email"
          placeholder="Email"
          className="login-input"
        />

        <input 
          type="password"
          placeholder="Password"
          className="login-input"
        />

        <div className="remember-row">
            <input type="checkbox"/>
            <span>Remember me</span>
        </div>

        <button className="signin-btn">
            Sign in
        </button>

        <div className="google-login">
            <GoogleLogin
                onSuccess={handleSuccess}
                onError={()=>console.log("Login failed")}
            />
        </div>

        <p className="forgot">Forgotten your password?</p>

    </div>

</div>

)
}

export default LoginPage;
