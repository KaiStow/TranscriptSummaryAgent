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
git clone https://github.com/KaiStow/TranscriptSummaryAgent.git
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

> **Note:** Installing PyAudio can be tricky on some systems.
- macOS: `brew install portaudio`
- Ubuntu: `sudo apt install portaudio19-dev`
- Windows: Use a precompiled PyAudio wheel

---

## 🔑 Environment Variables

This project uses a `.env` file to manage sensitive environment variables.

Inside of the `.env` file in the root of the project, add your Anthropic API key where specified in the code:

```env
ANTHROPIC_API_KEY="Anthropic API Key Here"
```

⚠️ **Do not commit your `.env` file to Git.**  
Make sure `.env` is included in your `.gitignore`.

---

## 🚀 Usage

Run the main script:

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

## 🗂️ Example Project Flow

```
Microphone Input
       ↓
Audio Recording (PyAudio)
       ↓
WAV File (wave)
       ↓
Speech Transcription
       ↓
Anthropic API
       ↓
AI-Generated Summary
```

---

## 📝 Example Output

**Transcript:**
> Today we discussed project timelines, upcoming deadlines, and blockers.

**Summary:**
> The speaker reviewed project timelines, deadlines, and current obstacles.

---

## 🧠 Use Cases

- Voice notes
- Meeting summaries
- Lecture recaps
- Personal voice journaling
- Voice-based assistants

---

## ⚠️ Notes & Limitations

- Audio quality depends on microphone input
- Transcription accuracy depends on the chosen STT model
- API usage may incur costs depending on your Anthropic plan

---

## 📌 Future Improvements

- Real-time transcription
- Speaker diarization
- Timestamped summaries
- GUI or web interface
- Support for multiple audio formats

---

## 📄 License

MIT License — feel free to use, modify, and distribute.
