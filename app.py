import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
import os
from dotenv import load_dotenv

# Load credentials
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(resume_text, jd, prompt):
    # Try the most likely model names in order of stability
    model_names = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
    
    for name in model_names:
        try:
            model = genai.GenerativeModel(name)
            full_query = f"{prompt}\n\nResume:\n{resume_text}\n\nJD:\n{jd}"
            response = model.generate_content(full_query)
            return response.text
        except Exception:
            continue # Try the next model if one fails
    return "Error: Could not connect to any Gemini models. Please check your API key and library version."

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        text += str(reader.pages[page].extract_text())
    return text

# UI Setup
st.set_page_config(page_title="SmartRes AI", page_icon="🚀")
st.title("Code the Future: AI Resume Analyzer")

with st.sidebar:
    st.header("Input Panel")
    jd = st.text_area("Target Job Description")
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if st.button("Analyze Resume"):
    if uploaded_file and jd:
        with st.spinner('🤖 AI is evaluating...'):
            resume_text = input_pdf_text(uploaded_file)
            
            # This prompt is engineered to win the hackathon requirements
            analysis_prompt = """
            As an expert ATS and Career Coach, provide:
            1. **Extracted Highlights**: Key skills and projects.
            2. **Resume Rating**: A score out of 10.
            3. **Professional Summary**: A STRICTLY 2-LINE summary.
            4. **Gap Analysis**: Missing skills from the JD.
            5. **Task**: One specific action to reach a score of 8/10.
            Format clearly in Markdown.
            """
            
            result = get_gemini_response(resume_text, jd, analysis_prompt)
            st.markdown(result)
    else:
        st.error("Please provide both the Resume and the JD.")
