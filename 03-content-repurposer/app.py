import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Content Repurposer", page_icon="✍️", layout="wide")
st.title("✍️ AI Content Repurposer")
st.caption("Turn one piece of content into Twitter threads, LinkedIn posts, emails, and scripts.")

with st.sidebar:
    api_key = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
    model = st.selectbox("Model", ["gpt-4o-mini", "gpt-4o"], index=0)

if not api_key:
    st.warning("Enter OpenAI API key in sidebar")
    st.stop()

client = OpenAI(api_key=api_key)

content = st.text_area("Paste your blog post, transcript, or long content here", height=250)

if st.button("Repurpose Content", type="primary") and content:
    with st.spinner("Creating multiple formats..."):
        prompt = f"""Take the following content and create:
1. A Twitter/X thread (8-12 tweets)
2. A professional LinkedIn post
3. A short email newsletter version
4. A YouTube video script outline

Content:
{content[:6000]}
"""
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        st.markdown(response.choices[0].message.content)
