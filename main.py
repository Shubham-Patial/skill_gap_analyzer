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

resume_text = ""
reader = PdfReader("resume.pdf")
for page in reader.pages:
    resume_text += page.extract_text().lower()
print(resume_text)

job_text = input("\nWRITE/PASTE JOB DESCRIPTION TEXT:\n").lower()

row = []
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

    row.append([skill, skill_in_resume, skill_in_job, status])
total_required = sum(1 for skill in SKILLS if re.search(r"\b" + re.escape(skill) + r"\b", job_text))
matched = sum(1 for skill in SKILLS if (re.search(r"\b" + re.escape(skill) + r"\b", resume_text) and re.search(r"\b" + re.escape(skill) + r"\b", job_text)))
if total_required > 0:
    score = (matched / total_required) * 100
else:
    score = 0
print("\nSkill Match %", f"{score:.1f}%")    
df = pd.DataFrame(row, columns=["Skill","Resume","Job","status"])
print("\n\nRESULT:\n")
print(df)