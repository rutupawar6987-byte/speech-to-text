# guinea_switch2_pix.py
# GenAI Voice-to-Text using Whisper

# guinea_switch2_pix.py
# GenAI Voice-to-Text using Whisper

import whisper
import os

# Mapping short codes to Whisper-supported language names
LANGUAGE_MAP = {
    "en": "english",
    "hi": "hindi",
    "fr": "french",
    "es": "spanish",
    "de": "german",
    "ja": "japanese",
    "ko": "korean",
    "zh": "chinese",
    # Add more codes if needed
}

def transcribe_audio(audio_path: str, output_path: str = None, language: str = None):
    """
    Transcribes audio to text using OpenAI Whisper model.

    Parameters:
    - audio_path: Path to the input audio file (mp3, m4a, wav, etc.)
    - output_path: Optional path to save transcription
    - language: Optional language code (e.g., "en", "hi") or full name
    """

    # Check if file exists
    if not os.path.isfile(audio_path):
        print("Error: Audio file not found.")
        return

    # Convert short code to Whisper-supported language name
    if language in LANGUAGE_MAP:
        language = LANGUAGE_MAP[language]

    # Load Whisper model
    print("Loading Whisper model...")
    model = whisper.load_model("small")  # tiny, base, medium, large

    # Transcribe
    print("Transcribing audio...")
    try:
        result = model.transcribe(audio_path, language=language)
        text = result["text"]
    except Exception as e:
        print(f"Error during transcription: {e}")
        return

    # Print transcription
    print("\n--- Transcription ---\n")
    print(text)
    print("\n--------------------\n")

    # Save to file if path provided
    if output_path:
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Transcription saved to: {output_path}")
        except Exception as e:
            print(f"Error saving transcription: {e}")

    return text

# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":
    audio_path = input("Enter the path to your audio file (mp3, m4a, wav, etc.): ").strip()
    output_path = input("Enter output file path to save transcription (e.g., output.txt) or press Enter to skip: ").strip()
    output_path = output_path if output_path else None
    language = input("Enter language code (e.g., 'en' for English, 'hi' for Hindi) or press Enter to auto-detect: ").strip()
    language = language if language else None

    transcribe_audio(audio_path, output_path, language)