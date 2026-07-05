import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from pypdf import PdfReader

# -----------------------------
# Configuration
# -----------------------------

st.set_page_config(
    page_title="PathWise AI",
    page_icon="🚀",
    layout="wide"
)
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stButton>button{
    width:100%;
    border-radius:10px;
    height:3em;
    font-size:18px;
    font-weight:bold;
}

div[data-testid="metric-container"]{
    background:#1E293B;
    padding:20px;
    border-radius:15px;
    border:1px solid #3B82F6;
}

h1,h2,h3{
    color:#4F9DFF;
}

</style>
""", unsafe_allow_html=True)

load_dotenv()

if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API Key not found!")
    st.stop()

genai.configure(api_key=api_key)
if not api_key:
    st.error("Gemini API Key not found!")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")
if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""
# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("🚀 PathWise AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📄 Resume Analyzer",
        "🗺️ Learning Roadmap",
        "💼 Internship Recommendations",
        "💬 AI Career Coach",
        "ℹ️ About"
    ]
)

# -----------------------------
# Dashboard
# -----------------------------

if page == "🏠 Dashboard":

    st.title("🚀 PathWise AI")

    st.subheader("Career Decision Intelligence Platform")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Career Readiness","82/100")

    with c2:
        st.metric("ATS Score","88/100")

    with c3:
        st.metric("Projects","4")

    with c4:
        st.metric("Certifications","3")

    st.divider()

    st.markdown("## 🚀 What PathWise AI can do")

    col1, col2 = st.columns(2)

    with col1:

        st.success("""
✅ Resume Analysis

✅ Skill Gap Detection

✅ Career Readiness

✅ Certification Suggestions

✅ Internship Recommendations
""")

    with col2:

        st.info("""
🤖 AI Career Coach

🗺️ Personalized Roadmap

📚 Learning Plan

🎯 Career Guidance

📈 Decision Intelligence
""")

    st.divider()

    st.markdown("### Getting Started")

    st.write(
        """
1. Open **Resume Analyzer**

2. Upload your Resume PDF

3. Click Analyze

4. Explore Roadmap

5. Ask the AI Coach
"""
    )

# -----------------------------
# Resume Analyzer
# -----------------------------

elif page == "📄 Resume Analyzer":

    st.title("📄 Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file:

        reader = PdfReader(uploaded_file)

        resume_text = ""

        for page_pdf in reader.pages:

            text = page_pdf.extract_text()

            if text:
                resume_text += text

            st.session_state.resume_text = resume_text
        st.success("Resume uploaded successfully!")

        if st.button("Analyze Resume"):

            with st.spinner("Analyzing Resume..."):

                prompt = f"""
You are an expert Career Coach.

Analyze the following resume.

Return the result in markdown.

Include:

# Resume Summary

# Career Readiness Score (0-100)

# Top Strengths

# Weaknesses

# Missing Skills

# Recommended Certifications

# Suggested Projects

# ATS Improvement Tips

Resume:

{resume_text}
"""

                response = model.generate_content(prompt)

                st.markdown(response.text)  
                
# Learning Roadmap
# -----------------------------

elif page == "🗺️ Learning Roadmap":

    st.title("🗺️ AI Learning Roadmap")

    career = st.selectbox(
        "Choose your target career",
        [
            "AI Engineer",
            "Data Scientist",
            "Machine Learning Engineer",
            "Software Engineer",
            "Cloud Engineer",
            "Cybersecurity Engineer",
            "Full Stack Developer"
        ]
    )

    experience = st.selectbox(
        "Current Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    if st.button("Generate Roadmap"):

        with st.spinner("Generating roadmap..."):

            prompt = f"""
Create a complete learning roadmap.

Target Career:
{career}

Current Level:
{experience}

Include:

# 30-Day Plan

# 90-Day Plan

# 6-Month Plan

# Skills

# Certifications

# Projects

# Interview Preparation

Return the result in markdown.
"""

            response = model.generate_content(prompt)

            st.markdown(response.text)

# -----------------------------
# Internship Recommendations
# -----------------------------

elif page == "💼 Internship Recommendations":

    st.title("💼 Internship Recommendation Engine")

    skills = st.text_area(
        "Enter your skills",
        placeholder="Python, SQL, Machine Learning..."
    )

    interests = st.text_input(
        "Career Interests",
        placeholder="AI, Data Science..."
    )

    if st.button("Recommend Internships"):

        with st.spinner("Finding recommendations..."):

            prompt = f"""
Recommend internships.

Skills:
{skills}

Interests:
{interests}

Return:

# Best Internship Roles

# Why These Roles

# Skills Missing

# Companies

# Certifications

# Resume Tips

# Interview Preparation
"""

            response = model.generate_content(prompt)

            st.markdown(response.text)

# -----------------------------
# AI Career Coach
# -----------------------------

elif page == "💬 AI Career Coach":

    st.title("💬 AI Career Coach")

    question = st.text_area(
        "Ask your career question"
    )

    if st.button("Ask AI Coach"):

        with st.spinner("Thinking..."):

            response = model.generate_content(question)

            st.markdown(response.text)

# -----------------------------
# About
# -----------------------------

elif page == "ℹ️ About":

    st.title("About PathWise AI")

    st.markdown("""
# 🚀 PathWise AI

An AI-Powered Career Decision Intelligence Platform.

## Features

- 📄 Resume Analyzer
- 📊 Career Dashboard
- 🗺️ Learning Roadmap
- 💼 Internship Recommendation Engine
- 💬 AI Career Coach

Built using:

- Google Gemini AI
- Streamlit
- Python
- Google AI Studio
""")