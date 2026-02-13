import streamlit as st
from pypdf import PdfReader
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("📄 AI Smart File Assistant")

# Upload PDFs
uploaded_files = st.file_uploader("Upload PDFs", accept_multiple_files=True)

question = st.text_input("Ask a question")

def extract_text(files):
    text = ""
    for file in files:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text


if st.button("Search"):

    if not uploaded_files:
        st.warning("Please upload PDFs first")
    elif not question:
        st.warning("Please ask a question")
    else:
        with st.spinner("Processing with AI..."):

            document_text = extract_text(uploaded_files)

            prompt = f"""
            Answer the question based only on the document content.

            Document:
            {document_text}

            Question:
            {question}
            """

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            answer = response.choices[0].message.content

            st.success("Answer:")
            st.write(answer)
