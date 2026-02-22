import streamlit as st
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API"))

prompt = """
You are a YouTube video summarizer.
Summarize the transcript into:
- Key points
- Important insights
- Final conclusion
Limit response to 250 words.
Transcript:
"""

def extract_video_id(url):
    parsed_url = urlparse(url)

    if parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]

    if parsed_url.hostname in ("www.youtube.com", "youtube.com"):
        return parse_qs(parsed_url.query)["v"][0]

    return None


def extract_transcript(video_id):
    try:
        api = YouTubeTranscriptApi()
        transcript_data = api.fetch(video_id)

        transcript = " ".join([chunk.text for chunk in transcript_data])
        return transcript

    except Exception as e:
        st.error("Could not fetch transcript. Video may not have captions.")
        return None


def generate_summary(transcript_text):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt + transcript_text[:15000])
    return response.text


st.title("🎬 YouTube Transcript to Smart Notes Converter")

youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = extract_video_id(youtube_link)

    if video_id:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

if st.button("Generate Notes"):
    if youtube_link:
        video_id = extract_video_id(youtube_link)

        if video_id:
            with st.spinner("Generating summary..."):
                transcript = extract_transcript(video_id)
                summary = generate_summary(transcript)

                st.markdown("## 📝 Detailed Notes")
                st.write(summary)
        else:
            st.error("Invalid YouTube URL")
