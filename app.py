import os
from dotenv import load_dotenv
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_video_id(youtube_url):
    if 'v=' in youtube_url:
        return youtube_url.split('v=')[1].split('&')[0]
    else:
        raise ValueError("Invalid YouTube URL format")

def get_transcript(video_id):

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id,languages=['en','en-US'])
        return transcript
    except TranscriptsDisabled:
        raise RuntimeError("Subtitles are disabled for this video.")
    except Exception as e:
        raise RuntimeError(f"Error fetching transcript: {e}")

def transcript_to_text(transcript):

    return " ".join([entry['text'] for entry in transcript])

def summarize_text(text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Summarize the youtube video based on this transcript: "+text)
    return response.text

def main():

    youtube_url = input("Enter the YouTube video URL: ")
    try:
        video_id = get_video_id(youtube_url)
        transcript = get_transcript(video_id)
        if not transcript:
            print("No transcript available for this video.")
            return
        text = transcript_to_text(transcript)
        summary = summarize_text(text)
        print("\nSummary:")
        print(summary)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
