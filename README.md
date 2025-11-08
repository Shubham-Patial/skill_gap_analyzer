# Skill Gap Analyzer – Resume vs Job Requirements

A simple AI-style tool that analyzes a resume PDF and compares it against a job description to identify missing skills, matched skills, and overall skill match %.

Built to help job seekers instantly understand where they stand — without manually reading every job posting.

### 🚀 Features
- Upload your resume PDF
- Paste any Job Description text
- Detect matching skills using Regex
- Calculates Skill Match %
- Categorizes skills into:
  - ✅ MATCH (you have it + job needs it)
  - ❌ MISSING (job needs it but resume doesn’t show it)
  - 🟡 NOT REQUIRED (you have it but job doesn't need it)
  - – (not relevant)

### 🧠 Tech Stack
| Area | Tools Used |
|------|------------|
| Language | Python |
| Skill Detection | Regex |
| PDF Parsing | PyPDF |
| UI | Streamlit |
| Data | Pandas |

### 📊 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

### 🔥 Why this project is valuable
This solves a real problem in job search — guessing if you're a match.

It shows:
- practical regex usage
- PDF parsing experience
- understanding of real job data
- end-to-end execution of a small AI-style product

### 🌐 Deployment (when ready)
This app can be deployed for free using Streamlit Cloud.

```
https://skillgapanalyzer-fvtqqgtpvrp6yubhaenjvh.streamlit.app/
```

---

### ⭐ Future Enhancements
- LLM skill extraction (OpenAI / Gemini)
- JD auto-scraper
- Skill recommendations
- Resume improvement suggestions

---

### Author
**Shubham Patial**
