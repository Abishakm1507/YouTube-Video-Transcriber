# 🎬 YouTube Transcript to Smart Notes Converter

An AI-powered Streamlit application that extracts YouTube video transcripts and generates structured, concise notes using Google's Gemini LLM.

---

## 🚀 Features

- 🔗 Accepts any valid YouTube URL
- 📄 Automatically extracts video transcript
- 🤖 Generates structured summary using Gemini
- 📝 Provides:
  - Key Points
  - Important Insights
  - Final Conclusion
- 🖼 Displays video thumbnail
- ⚡ Fast and simple UI built with Streamlit

---

## 🛠 Tech Stack

- Python
- Streamlit
- YouTube Transcript API
- Google Gemini (google-generativeai)
- python-dotenv

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Abishakm1507/YouTube-Video-Transcriber
cd YouTube-Video-Transcriber

```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Setup Environment Variables
Create a .env file in the root directory:

```bash
GEMINI_API=your_gemini_api_key_here
```
### 5. Run the Application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. User provides a YouTube URL.
2. The application extracts the Video ID from the URL.
3. The transcript is fetched using the YouTube Transcript API.
4. The transcript text is sent to Google Gemini LLM.
5. The model generates a structured summary (limited to 250 words).
6. The generated notes are displayed in the Streamlit UI.
