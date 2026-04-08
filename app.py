import streamlit as st
import whisper
import tempfile
import os

# ---------------- CONFIG ----------------
st.set_page_config(page_title="GenAI Speech-to-Text Pro", layout="centered")

st.title("🎤 GenAI Speech-to-Text PRO")
st.markdown("🚀 Upload / Record → Transcribe → Translate → Download")

# ---------------- LANGUAGE MAP ----------------
LANGUAGE_MAP = {
    "auto": None,
    "en": "english",
    "hi": "hindi",
    "fr": "french",
    "es": "spanish",
    "de": "german",
    "ja": "japanese",
    "ko": "korean",
    "zh": "chinese",
}

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Settings")

language = st.sidebar.selectbox("Language", list(LANGUAGE_MAP.keys()))
translate = st.sidebar.checkbox("🌍 Translate to English")
show_timestamps = st.sidebar.checkbox("⏱️ Show Timestamps")

# ---------------- INPUT ----------------
option = st.radio("Choose Input:", ["Upload Audio", "Record Audio"])

audio_path = None

# Upload
if option == "Upload Audio":
    audio_file = st.file_uploader("Upload Audio", type=["mp3", "wav", "m4a"])
    if audio_file:
        st.audio(audio_file)
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(audio_file.read())
            audio_path = tmp.name

# Record
else:
    audio_file = st.audio_input("Record your voice")
    if audio_file:
        st.audio(audio_file)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_file.read())
            audio_path = tmp.name

# ---------------- HELPER FUNCTIONS ----------------
def format_timestamp(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hrs:02}:{mins:02}:{secs:02}"

def generate_srt(segments):
    srt = ""
    for i, seg in enumerate(segments):
        start = format_timestamp(seg['start'])
        end = format_timestamp(seg['end'])
        text = seg['text']
        srt += f"{i+1}\n{start} --> {end}\n{text}\n\n"
    return srt

# ---------------- TRANSCRIBE ----------------
if audio_path:
    if st.button("🚀 Process Audio"):

        st.info("⏳ Processing...")

        try:
            lang = LANGUAGE_MAP[language]

            result = model.transcribe(
                audio_path,
                language=lang,
                task="translate" if translate else "transcribe"
            )

            text = result["text"]
            segments = result.get("segments", [])

            st.success("✅ Done!")

            # -------- TEXT OUTPUT --------
            st.subheader("📄 Transcription")
            st.write(text)

            # -------- TIMESTAMPS --------
            if show_timestamps and segments:
                st.subheader("⏱️ Timestamps")
                for seg in segments:
                    st.write(f"[{format_timestamp(seg['start'])}] {seg['text']}")

            # -------- DOWNLOAD TXT --------
            st.download_button(
                "⬇️ Download TXT",
                data=text,
                file_name="transcription.txt"
            )

            # -------- DOWNLOAD SRT --------
            if segments:
                srt_data = generate_srt(segments)

                st.download_button(
                    "⬇️ Download Subtitles (SRT)",
                    data=srt_data,
                    file_name="subtitles.srt"
                )

        except Exception as e:
            st.error(f"❌ Error: {e}")

        finally:
            if os.path.exists(audio_path):
                os.remove(audio_path)