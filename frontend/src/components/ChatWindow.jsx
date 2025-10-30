//src
import React, { useEffect, useRef } from "react";

export default function ChatWindow({ messages, input, setInput, handleSend }) {
  const bottomRef = useRef(null);

  // Scroll to the latest message whenever messages change
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div
      style={{
        flex: 1,
        display: "flex",
        flexDirection: "column",
        backgroundColor: "#fff",
      }}
    >
      {/* Chat Messages */}
      <div
        style={{
          flex: 1,
          padding: "20px",
          overflowY: "auto",
        }}
      >
        {messages.map((msg, idx) => (
          <div
            key={idx}
            style={{
              marginBottom: "10px",
              padding: "10px",
              borderRadius: "10px",
              maxWidth: "70%",
              backgroundColor: msg.role === "user" ? "#D0E6FF" : "#F1F1F1",
              alignSelf: msg.role === "user" ? "flex-end" : "flex-start",
            }}
          >
            <b>{msg.role === "user" ? "You" : "Assistant"}:</b> {msg.content}
          </div>
        ))}
        <div ref={bottomRef}></div>
      </div>

      {/* Input Box */}
      <div
        style={{
          display: "flex",
          borderTop: "2px solid #ccc",
          padding: "10px",
        }}
      >
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
          style={{
            flex: 1,
            padding: "10px",
            fontSize: "14px",
            border: "1px solid #ccc",
            borderRadius: "4px 0 0 4px",
            outline: "none",
          }}
        />
        <button
          onClick={handleSend}
          style={{
            padding: "10px 20px",
            fontSize: "14px",
            border: "none",
            backgroundColor: "#1a73e8",
            color: "white",
            cursor: "pointer",
            borderRadius: "0 4px 4px 0",
          }}
        >
          Send
        </button>
      </div>
    </div>
  );
}
