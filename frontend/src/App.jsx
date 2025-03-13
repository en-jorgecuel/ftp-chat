import React, { useState, useEffect } from "react";
import axios from "axios";

const API_URL = "http://localhost:8000/ws";

const Chat = ({ channel, user }) => {
  const [messages, setMessages] = useState([]);
  const [message, setMessage] = useState("");
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    const ws = new WebSocket(`${API_URL}/${channel}/${user}`);
    setSocket(ws);

    ws.onmessage = (event) => {
      setMessages(JSON.parse(event.data));
    };

    return () => ws.close();
  }, [channel, user]);

  const sendMessage = () => {
    if (socket && message.trim()) {
      socket.send(message);
      setMessage("");
    }
  };

  return (
    <div>
      <h2>Chat - {channel}</h2>
      <div style={{ height: "300px", overflowY: "scroll", border: "1px solid #ddd", padding: "10px" }}>
        {messages.map((msg, index) => (
          <div key={index}><b>{msg.user}</b>: {msg.message}</div>
        ))}
      </div>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type a message..."
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
};

const ChatApp = () => {
  const [channel, setChannel] = useState("general");
  const [user, setUser] = useState("User" + Math.floor(Math.random() * 1000));

  return (
    <div>
      <h1>FTP Chat (OldSchool Edition)</h1>
      <label>Channel: </label>
      <select onChange={(e) => setChannel(e.target.value)} value={channel}>
        <option value="general">General</option>
        <option value="team">Team</option>
        <option value="random">Random</option>
      </select>
      <Chat channel={channel} user={user} />
    </div>
  );
};

export default ChatApp;