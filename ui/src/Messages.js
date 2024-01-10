import React from "react";
import "./style.css";
import Message from "./Message";

const Messages = ({ messages }) => {
  
  return (
    <div className="messagesSection">
      {messages.map((message, idx) => {
        return (
          <div className="messagesContainer" key={idx}>
            <Message message={message} idx={idx}/>
          </div>
        );
      })}
    </div>
  );
};

export default Messages;