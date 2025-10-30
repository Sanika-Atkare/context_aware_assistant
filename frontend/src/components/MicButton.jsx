import React from "react";

const MicButton = () => {
  const startListening = () => {
    alert("Voice input not set up yet!");
  };

  return (
    <button onClick={startListening} style={{ marginTop: "10px", padding: "6px 12px", borderRadius: "5px" }}>
      🎤 Start Talking
    </button>
  );
};

export default MicButton;
