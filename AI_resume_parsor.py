import pdfplumber
import spacy
import re

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Skills List
skills_list = [
    "Python",
    "Java",
    "C",
    "C++",
    "HTML",
    "CSS",
    "JavaScript",
    "SQL",
    "Flask",
    "Django",
    "Machine Learning",
    "Data Science",
    "Git",
    "GitHub"
]

# Education Keywords
education_keywords = [
    "B.Tech",
    "B.E",
    "M.Tech",
    "MCA",
    "BCA",
    "MBA",
    "Bachelor",
    "Master"
]

def extract_text(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    return text


def extract_name(text):
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return "Not Found"


def extract_email(text):
    email = re.findall(r'[\w\.-]+@[\w\.-]+', text)

    if email:
        return email[0]

    return "Not Found"


def extract_phone(text):
    phone = re.findall(r'\+?\d[\d -]{8,12}\d', text)

    if phone:
        return phone[0]

    return "Not Found"


def extract_skills(text):

    found = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found.append(skill)

    return found


def extract_education(text):

    found = []

    for edu in education_keywords:
        if edu.lower() in text.lower():
            found.append(edu)

    return found


pdf_path = pdf_path = input("Enter PDF path: ")
resume_text = extract_text(pdf_path)

print("Name:", extract_name(resume_text))
print("Email:", extract_email(resume_text))
print("Phone:", extract_phone(resume_text))
print("Skills:", extract_skills(resume_text))
print("Education:", extract_education(resume_text))