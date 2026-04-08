import streamlit as st
import whisper
import tempfile

LANGUAGE_MAP = {
    "en": "english",
    "hi": "hindi",
    "fr": "french",
    "es": "spanish",
    "de": "german",
    "ja": "japanese",
    "ko": "korean",
    "zh": "chinese",
}

st.title("🎤 GenAI Speech-to-Text")
st.write("Upload an audio file to transcribe")

audio_file = st.file_uploader("Upload Audio", type=["mp3", "wav", "m4a"])

language = st.selectbox("Select Language", ["auto"] + list(LANGUAGE_MAP.keys()))

@st.cache_resource
def load_model():
    return whisper.load_model("base")  # IMPORTANT (not small)

if audio_file:
    st.audio(audio_file)

    if st.button("Transcribe"):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(audio_file.read())
            path = tmp.name

        st.write("⏳ Processing...")

        model = load_model()

        lang = None if language == "auto" else LANGUAGE_MAP[language]

        result = model.transcribe(path, language=lang)

        st.success("✅ Transcription Complete")
        st.write(result["text"])