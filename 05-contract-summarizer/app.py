import streamlit as st
from openai import OpenAI
from pypdf import PdfReader
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Contract Summarizer", page_icon="📝")
st.title("📝 AI Contract Summarizer")
st.caption("Upload a contract → get plain-English summary + risk highlights.")

api_key = st.sidebar.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
if not api_key:
    st.warning("Enter OpenAI API key")
    st.stop()

client = OpenAI(api_key=api_key)
uploaded = st.file_uploader("Upload Contract (PDF)", type=["pdf"])

if uploaded and st.button("Summarize", type="primary"):
    reader = PdfReader(uploaded)
    text = "".join([p.extract_text() or "" for p in reader.pages])[:12000]

    with st.spinner("Analyzing contract..."):
        prompt = f"""Summarize this contract in plain English.
Also list:
- Key obligations
- Payment terms
- Termination clauses
- Potential risks or red flags

Contract:
{text}
"""
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        st.markdown(response.choices[0].message.content)
