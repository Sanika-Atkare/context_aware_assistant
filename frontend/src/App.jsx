// src/App.jsx
import React, { useState } from "react";
import ChatWindow from "./components/ChatWindow.jsx";
import MemoryPanel from "./components/MemoryPanel.jsx";
import { sendMessageToBackend } from "./api.js";
import "./index.css";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = input;
    setInput("");

    // Add user message to chat
    setMessages((prev) => [...prev, { role: "user", content: userMessage }]);

    // Get assistant reply from backend
    const reply = await sendMessageToBackend(userMessage);

    // Add assistant reply to chat
    setMessages((prev) => [...prev, { role: "assistant", content: reply }]);
  };

  return (
    <div style={{ display: "flex", height: "100vh" }}>
      <MemoryPanel messages={messages} />
      <ChatWindow
        messages={messages}
        input={input}
        setInput={setInput}
        handleSend={handleSend}
      />
    </div>
  );
}

export default App;
