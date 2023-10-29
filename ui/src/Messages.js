import React from "react";
import "./style.css";
import Message from "./Message";

const Messages = ({ messages }) => {
  
  return (
    <div className="messagesSection">
      {messages.map(message => {
        return (
          <div className="messagesContainer">
            <Message message={message} />
          </div>
        );
      })}
    </div>
  );
};

export default Messages;