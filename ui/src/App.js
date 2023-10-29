import React from "react";
import "./style.css";
import Chat from "./Chat"

export default function App() {
  return (
    <div className="mainSection">
      <div className="heading">
        <img src="./larry.avif" className="larry-avatar"/>
        <span>larry.ai</span>
      </div>  
      <Chat />
    </div>
  );
}