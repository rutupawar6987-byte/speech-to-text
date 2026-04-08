
✨ GenAI Voice-to-Text Transcription System ✨
=============================================

📄 Project Overview:
A voice-to-text transcription system powered by **OpenAI Whisper**, converting audio files into text efficiently. Supports multiple audio formats and languages, working offline with local models.

🛠️ Features:
- ✅ Converts speech to text with high accuracy
- ✅ Supports audio formats: MP3, M4A, WAV, OGG, FLAC
- ✅ Supports multiple languages and accents
- ✅ Offline transcription using local Whisper models
- ✅ Enhanced from a simpler Google Speech Recognition version

⚙️ Dependencies:
- Python 3.x
- `openai-whisper`
- `torch`
- `pydub`
- `ffmpeg` (required for non-WAV files)

💻 Installation:
```bash
pip install openai-whisper torch pydub


Download FFmpeg: https://ffmpeg.org/download.html

1.Navigate to the project folder:

    cd path/to/voice-to-text

2. Run the scripts
     python genai_spech_to_text.py

3.Follow the prompts

    Enter the input audio file path

    Enter the output text file path

    Enter the language code (e.g., en-US)

4>Transcription is saved in the output file and displayed on screen

🌐 Supported Languages (Partial List):

# English (US) – en-US

# English (UK) – en-GB

# French – fr-FR

# German – de-DE

# Spanish – es-ES

# Italian – it-IT

# Japanese – ja-JP

# Korean – ko-KR

# Mandarin Chinese – zh-CN

# Russian – ru-RU

Whisper supports many more languages – see the official Whisper docs
5.⚡ How It Works:

Loads the audio file using Pydub and converts to WAV if necessary

Loads the OpenAI Whisper model (small/medium/large)

Transcribes audio to text locally

Saves the text to the output file

🎯 Use Cases:

Automatic transcription for interviews, podcasts, lectures

Generating subtitles and captions for videos

Research and content creation

Voice-driven AI applications

🛠️ Skills & Tools:
Python, PyTorch, OpenAI Whisper, FFmpeg, Pydub
Generative AI, NLP, Speech Recognition, Audio Processing

📜 License:
This project is licensed under the MIT License




