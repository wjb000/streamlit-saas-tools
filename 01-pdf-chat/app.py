import streamlit as st
from openai import OpenAI
from pypdf import PdfReader
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI PDF Chat", page_icon="📄", layout="wide")
st.title("📄 AI PDF Chat")
st.caption("Upload a PDF and ask questions about it. Perfect starter for a paid product.")

# Sidebar
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
    model = st.selectbox("Model", ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"], index=0)
    st.markdown("---")
    st.markdown("**How to monetize later:**")
    st.markdown("- Add login")
    st.markdown("- Add Stripe")
    st.markdown("- Limit free uses")

if not api_key:
    st.warning("Please enter your OpenAI API key in the sidebar to continue.")
    st.stop()

client = OpenAI(api_key=api_key)

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

# Upload
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n\n"
    st.session_state.pdf_text = text[:50000]  # limit for context
    st.success(f"PDF loaded ({len(reader.pages)} pages). You can now ask questions.")

# Chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask a question about the PDF..."):
    if not st.session_state.pdf_text:
        st.error("Please upload a PDF first.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that answers questions based only on the provided PDF content. If the answer is not in the document, say so clearly."},
                        {"role": "user", "content": f"PDF Content:\n\n{st.session_state.pdf_text}\n\nQuestion: {prompt}"}
                    ],
                    temperature=0.2,
                )
                answer = response.choices[0].message.content
                st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
