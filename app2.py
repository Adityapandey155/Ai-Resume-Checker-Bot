import streamlit as st
from pdfminer.high_level import extract_text
import re

def extract_text_from_pdf(pdf_file):
    return extract_text(pdf_file)

def extract_contact_info(text):
    email = re.findall(r'\S+@\S+', text)
    phone = re.findall(r'\+?\d[\d -]{8,}\d', text)
    return {"Email": email[0] if email else "Not found", "Phone": phone[0] if phone else "Not found"}

def extract_skills(text):
    skills_list = ["Python", "Java", "SQL", "Machine Learning", "Excel", "Communication", "Leadership"]
    found_skills = [skill for skill in skills_list if skill.lower() in text.lower()]
    return found_skills

def score_resume(skills_found):
    return min(100, len(skills_found) * 10)

# Streamlit UI
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("🧠 AI Resume Analyzer")
st.write("Upload your resume to get an AI-powered analysis and feedback.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    
    st.subheader("📄 Extracted Text")
    with st.expander("Show/Hide Text"):
        st.write(text)
    
    st.subheader("📊 Resume Analysis")
    contact_info = extract_contact_info(text)
    st.write(f"**Email:** {contact_info['Email']}")
    st.write(f"**Phone:** {contact_info['Phone']}")
    
    skills_found = extract_skills(text)
    st.write(f"**Skills Detected:** {', '.join(skills_found) if skills_found else 'None'}")
    
    resume_score = score_resume(skills_found)
    st.progress(resume_score)
    st.write(f"**Resume Score:** {resume_score}/100")

    if resume_score < 60:
        st.warning("Consider improving your resume with more technical and soft skills.")
    else:
        st.success("Great! Your resume shows strong relevant skills.")

# Footer
st.markdown("---")
st.markdown("⭐️ Built with Streamlit | [GitHub](https://github.com/YOUR_USERNAME/resume-analyzer) | © 2025")