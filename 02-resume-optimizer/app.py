import streamlit as st
from openai import OpenAI
from pypdf import PdfReader
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Resume Optimizer", page_icon="📄", layout="wide")
st.title("📄 AI Resume Optimizer")
st.caption("Upload your resume and get a score + improved version tailored to a job.")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
    model = st.selectbox("Model", ["gpt-4o-mini", "gpt-4o"], index=0)

if not api_key:
    st.warning("Enter your OpenAI API key in the sidebar.")
    st.stop()

client = OpenAI(api_key=api_key)

col1, col2 = st.columns(2)

with col1:
    uploaded = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    job_title = st.text_input("Target Job Title", placeholder="e.g. Senior Product Manager")
    job_desc = st.text_area("Paste Job Description (optional but recommended)", height=150)

resume_text = ""
if uploaded:
    reader = PdfReader(uploaded)
    for page in reader.pages:
        t = page.extract_text()
        if t:
            resume_text += t + "\n"

if st.button("Optimize Resume", type="primary") and resume_text and job_title:
    with st.spinner("Analyzing and rewriting..."):
        prompt = f"""You are an expert resume writer and recruiter.

Resume:
{resume_text[:8000]}

Target Job: {job_title}
Job Description: {job_desc or "Not provided"}

Please provide:
1. Overall score out of 100 with short explanation
2. Top 5 strengths
3. Top 5 weaknesses / missing keywords
4. A fully rewritten, improved version of the resume optimized for this job (keep it professional and truthful)
"""
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
        )
        result = response.choices[0].message.content

    st.markdown("---")
    st.subheader("Results")
    st.markdown(result)
elif st.button("Optimize Resume", type="primary"):
    st.error("Please upload a resume and enter a target job title.")
