import React from "react";

const MemoryPanel = ({ messages }) => {
  return (
    <div className="memory-panel">
      <h3>Memory Store</h3>
      {/* Optional: just show the last 5 messages */}
      {messages.slice(-5).map((msg, index) => (
        <div key={index} className={msg.role}>
          {msg.role}: {msg.content}
        </div>
      ))}
    </div>
  );
};

export default MemoryPanel;
