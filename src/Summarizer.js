import React, { useState } from "react";
import axios from "axios";

const Summarizer = () => {
  const [url, setUrl] = useState("");
  const [summary, setSummary] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:5000/summarize", {
        youtube_url: url,
      });
      setSummary(response.data.summary);
      setError("");
    } catch (err) {
      setError(err.response ? err.response.data.error : "An error occurred");
      setSummary("");
    }
  };

  return (
    <div>
      <h1>YouTube Video Summarizer</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Enter YouTube URL"
          required
        />
        <button type="submit">Summarize</button>
      </form>
      {summary && (
        <div>
          <h2>Summary:</h2>
          <p>{summary}</p>
        </div>
      )}
      {error && (
        <div>
          <h2>Error:</h2>
          <p>{error}</p>
        </div>
      )}
    </div>
  );
};

export default Summarizer;
