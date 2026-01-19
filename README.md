# 🎙️ Audio Recorder & AI Summarizer

An end-to-end Python project that records microphone audio, saves it as a WAV file, transcribes the speech into text, and uses the Anthropic API to generate a concise summary of what was said.

---

## ✨ Features

- Record live microphone audio using **PyAudio**
- Save recordings as **WAV** files with Python’s `wave` module
- Transcribe audio into text
- Send transcripts to the **Anthropic API** for AI-powered summarization
- Simple, modular pipeline that’s easy to extend

---

## 🛠️ Tech Stack

- Python 3.9+
- PyAudio
- wave
- Speech-to-text (your chosen transcription method)
- Anthropic API (Claude)

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

This project uses a `.env` file to manage sensitive environment variables.

Create a `.env` file in the root of the project and add your Anthropic API key where specified in the code:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

⚠️ **Do not commit your `.env` file to Git.**  
Make sure `.env` is included in your `.gitignore`.

---

## 🚀 Usage

```bash
python main.py
```

The program will:
1. Record audio from your microphone
2. Save it as a `.wav` file
3. Transcribe the audio into text
4. Send the transcript to the Anthropic API
5. Output a summarized version of the speech

---

## 📄 License

MIT License
