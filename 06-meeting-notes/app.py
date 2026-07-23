import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Meeting Notes", page_icon="🎙️")
st.title("🎙️ AI Meeting Notes Organizer")
st.caption("Paste transcript → get summary, action items, and follow-up emails.")

api_key = st.sidebar.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
if not api_key:
    st.warning("Enter OpenAI API key")
    st.stop()

client = OpenAI(api_key=api_key)
transcript = st.text_area("Paste meeting transcript", height=250)

if st.button("Organize Notes", type="primary") and transcript:
    with st.spinner("Processing..."):
        prompt = f"""From this meeting transcript, create:
1. Concise summary (bullet points)
2. Action items with owners (if mentioned)
3. Key decisions made
4. Suggested follow-up email

Transcript:
{transcript[:8000]}
"""
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        st.markdown(response.choices[0].message.content)
