import streamlit as st
from pypdf import PdfReader
import pandas as pd
import re

SKILLS = [
    "python","pandas","numpy","sql","postgresql","mysql",
    "excel","power bi","tableau","data visualization",
    "statistics","a/b testing","etl","regex","json","csv",
    "matplotlib","seaborn","scikit-learn","machine learning",
    "aws","s3","azure","bigquery","data cleaning","data wrangling",
    "power query","dax"
]

st.title("Skill Gap Analyzer – Resume vs Job Description")
st.info("📄 Upload your resume (PDF) and paste the job description to see your skill match score.")
resume_file = st.file_uploader("Upload your resume PDF", type=["pdf"])

job_text = st.text_area("Paste Job Description here").lower()

if st.button("Analyze"):
    if resume_file is None:
        st.error("Please upload a resume PDF.")
    else:
        reader = PdfReader(resume_file)
        resume_text = ""
        for page in reader.pages:
            resume_text += page.extract_text().lower()

        rows = []
        for skill in SKILLS:
            pattern = r"\b" + re.escape(skill) + r"\b"
            skill_in_resume = re.search(pattern, resume_text) is not None
            skill_in_job = re.search(pattern, job_text) is not None

            if skill_in_resume and skill_in_job:
                status = "MATCH"
            elif (not skill_in_resume) and skill_in_job:
                status = "MISSING"
            elif skill_in_resume and (not skill_in_job):
                status = "NOT REQUIRED"
            else:
                status = "-"

            rows.append([skill, skill_in_resume, skill_in_job, status])

        total_required = sum(1 for skill in SKILLS if re.search(r"\b" + re.escape(skill) + r"\b", job_text))

        matched = sum(1 for skill in SKILLS if (re.search(r"\b" + re.escape(skill) + r"\b", resume_text) and re.search(r"\b" + re.escape(skill) + r"\b", job_text)))
        if total_required > 0:
            score = (matched / total_required) * 100
        else:
            score = 0
        st.metric("Skill Match %", f"{score:.1f}%")

        df = pd.DataFrame(rows, columns=["Skill","Resume","Job","Status"])
        df["Resume"] = df["Resume"].map({True:"✅", False:"❌"})
        df["Job"]    = df["Job"].map({True:"✅", False:"❌"})
        st.dataframe(df)
