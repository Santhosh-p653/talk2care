import streamlit as st
import requests

AI_WORKER_URL = "http://ai_worker:8000/transcribe"
BACKEND_SUMMARY_URL = "http://backend:5000/summarize"

st.set_page_config(page_title="Talk2Care")

st.title("🎙️ Talk2Care")
st.write("Upload an audio file to generate transcript and summary")

uploaded_file = st.file_uploader(
    "Upload audio file",
    type=["wav", "mp3", "m4a"]
)

if uploaded_file and st.button("Process"):

    st.audio(uploaded_file)

    with st.spinner("Transcribing audio..."):
        try:
            resp = requests.post(
                AI_WORKER_URL,
                files={"file": uploaded_file}
            )
            resp.raise_for_status()
            transcript = resp.json()["transcript"]
        except Exception as e:
            st.error(f"Transcription failed: {e}")
            st.stop()

    st.subheader("📝 Transcript")
    st.write(transcript)

    with st.spinner("Generating summary..."):
        try:
            resp = requests.post(
                BACKEND_SUMMARY_URL,
                json={"text": transcript}
            )
            resp.raise_for_status()
            summary = resp.json()["summary"]
        except Exception as e:
            st.error(f"Summarization failed: {e}")
            st.stop()

    st.subheader("📌 Summary")
    st.write(summary)
