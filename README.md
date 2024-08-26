# YouTube Summarizer

A web application that generates summaries of YouTube videos using their transcripts. The backend is powered by Flask, and the frontend is built with React. It uses gemini 1.5 flash API to summarize.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Node.js
- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/UdayrajJhala/YoutubeSummarizer.git
   cd YoutubeSummarizer

2. **Set up the backend:**

- Install the required Python packages:

  ```bash
  pip install Flask Flask-CORS python-dotenv google-generativeai youtube-transcript-api

3. **Setup the frontend**

- Navigate to the project directory and install dependencies:

  ```bash
  npm install

4. **Configure environment variables:**
- Create a .env file in the root directory and add your Google API key:
   ```bash
   GOOGLE_API_KEY=your_google_api_key

### Running the application

1. **Start the backend server**
    ```bash
    python app.py

2. **Start the frontend:**
   ```bash
   npm start
The app will run on http://localhost:3000.

- Enter the YouTube video URL in the input field and click on "Summarize" to get the video summary.
- Only works with english videos for now
- paste a link of this form - https://www.youtube.com/watch?v=d24s21421814
- https://youtu.be/23u2483dsfw?si=du28yd893h89fh - this type of link, which is generated using share button, wont work.


