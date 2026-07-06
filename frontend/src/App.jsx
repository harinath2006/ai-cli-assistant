import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  async function sendMessage() {
    if (message.trim() === "") return;

    setLoading(true);

    try {
          const API_URL = import.meta.env.VITE_API_URL;
          const res = await axios.post(
            `${API_URL}/chat`,
            {
              message: message,
            }
          );

      setResponse(res.data.response);
    } catch (error) {
      console.error(error);
      setResponse("❌ Could not connect to the backend.");
    }

    setLoading(false);
  }

  return (
    <div className="container">
      <h1>🤖 AI Assistant</h1>

      <textarea
        rows="5"
        placeholder="Ask me anything..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button onClick={sendMessage}>Send</button>

      {loading && <p>Thinking...</p>}

      {response && (
        <div className="response">
          <h3>Response</h3>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}

export default App;