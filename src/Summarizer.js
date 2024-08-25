// src/Summarizer.js
import React, { useState } from "react";
import axios from "axios";
import ReactMarkdown from "react-markdown";
import "./Summarizer.css";

function Summarizer() {
  const [youtubeUrl, setYoutubeUrl] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setSummary("");

    try {
      const response = await axios.post("http://localhost:5000/summarize", {
        youtube_url: youtubeUrl,
      });
      setSummary(response.data.summary);
    } catch (err) {
      console.log(err);
      setError("An error occurred while summarizing the video.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>YouTube Video Summarizer</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter YouTube URL"
          value={youtubeUrl}
          onChange={(e) => setYoutubeUrl(e.target.value)}
          required
        />
        <button type="submit" disabled={loading}>
          {loading ? "Summarizing..." : "Summarize"}
        </button>
      </form>
      {error && <div className="error">{error}</div>}
      {summary && (
        <div className="summary">
          <h2>Summary:</h2>
          <ReactMarkdown>{summary}</ReactMarkdown>
        </div>
      )}
    </div>
  );
}

export default Summarizer;
