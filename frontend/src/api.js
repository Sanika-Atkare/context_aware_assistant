export const sendMessageToBackend = async (message) => {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/message", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_message: message }), // ✅ key must match backend
    });

    const data = await res.json();
    return data.reply; // ✅ return the reply string directly
  } catch (err) {
    console.error(err);
    return "Backend not reachable."; // ✅ return string for display
  }
};
