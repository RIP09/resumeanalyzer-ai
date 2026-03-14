import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
import os

# 1. SETUP - REPLACE THE KEY BELOW WITH YOUR ACTUAL API KEY
# (Do this just for the demo to ensure it runs, then remove before final public share if desired)
os.environ["GOOGLE_API_KEY"] = "YOUR_ACTUAL_GEMINI_API_KEY_HERE"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def get_gemini_response(resume_text, jd, prompt):
    # This list covers the most common model names currently active
    for model_name in ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']:
        try:
            model = genai.GenerativeModel(model_name)
            full_query = f"{prompt}\n\nResume:\n{resume_text}\n\nJD:\n{jd}"
            response = model.generate_content(full_query)
            return response.text
        except Exception:
            continue
    return "AI Error: Please check API Key/Network."

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        text += str(reader.pages[page].extract_text())
    return text

# 2. UI CODE
st.set_page_config(page_title="SmartRes AI", layout="centered")
st.title("🚀 Code the Future: AI Resume Analyzer")

jd = st.text_area("Paste Job Description (JD)")
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if st.button("Analyze Resume"):
    if uploaded_file and jd:
        with st.spinner('AI is evaluating...'):
            resume_text = input_pdf_text(uploaded_file)
            analysis_prompt = """
            As an expert Recruiter, provide:
            1. Resume Rating (out of 10).
            2. Extracted Highlights (Skills/Projects).
            3. A STRICTLY 2-LINE Professional Summary.
            4. Gap Analysis (Missing skills from JD).
            5. Improvement Task to reach 8/10 score.
            """
            result = get_gemini_response(resume_text, jd, analysis_prompt)
            st.markdown(result)
    else:
        st.error("Missing Resume or JD.")
