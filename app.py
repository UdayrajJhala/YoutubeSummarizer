from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

app = Flask(__name__)
CORS(app) 

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_video_id(youtube_url):
    if 'v=' in youtube_url:
        return youtube_url.split('v=')[1].split('&')[0]
    else:
        raise ValueError("Invalid YouTube URL format")

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'en-US', 'en-GB'])
        return transcript
    except TranscriptsDisabled:
        raise RuntimeError("Subtitles are disabled for this video.")
    except Exception as e:
        raise RuntimeError(f"Error fetching transcript: {e}")

def transcript_to_text(transcript):
    return " ".join([entry['text'] for entry in transcript])

def summarize_text(text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Summarize the youtube video based on this transcript: " + text)
    return response.text

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    youtube_url = data.get("youtube_url")
    try:
        video_id = get_video_id(youtube_url)
        transcript = get_transcript(video_id)
        if not transcript:
            return jsonify({"error": "No transcript available for this video."}), 400
        text = transcript_to_text(transcript)
        summary = summarize_text(text)
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
