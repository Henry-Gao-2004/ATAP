import json
import ndjson
from typing import Tuple
import requests
import google.generativeai as genai

base_url = "http://localhost:11434"

api_key = open("api_key.txt", "r").read().strip()
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

def is_application(email: str) -> Tuple[bool, str]:
    email = json.loads(email)
    subject = email["subject"]
    body = email["text"]
    prompt = "Return 'True' if the following email is application related, and return 'False' otherwise. Subject is " + subject + " and body is " + body
    response = model.generate_content(prompt)
    return True, response.text.strip()

def classify_email(email: str) -> Tuple[bool, str]:
    email = json.loads(email)
    subject = email["subject"]
    body = email["text"]
    prompt = "Categorize the email into one of the categories: 'confirmation', 'update', 'posting'. Only return the category. Subject is " + subject + " and body is " + body
    response = model.generate_content(prompt)
    return True, response.text.strip()

def extract_info(email: str) -> Tuple[bool, list[str]]:
    email = json.loads(email)
    subject = email["subject"]
    body = email["text"]
    prompt = "Extract and return the company, position and date in format YYYYMMDD separated with comma. If company is unknown, let company be 'Unknown Company'. If position is unknown, let position be 'Unknown Position'. Do not return anything else. Subject is " + subject + " and body is " + body
    response = model.generate_content(prompt)
    return True, response.text.strip().split(",")

def classify_category(email: str) -> Tuple[bool, str]:
    email = json.loads(email)
    subject = email["subject"]
    body = email["text"]
    prompt = "Classify the email into one of the following categories based on its primary content: 'Internship', 'Club', 'Education', or 'Scholarship'. Respond with one word only, selecting the most appropriate category. Subject is " + subject + " and body is " + body
    response = model.generate_content(prompt)
    return True, response.text.strip()

def email_action(email: str) -> Tuple[bool, str]:
    email = json.loads(email)
    subject = email["subject"]
    body = email["text"]
    prompt = "Categorize the email into one of the following categories: 'confirmation', 'assessment_invite', 'assessment_confirmation', 'interview_invite', 'interview_confirmation', 'rejection', “decision_update”. Return 'rejection' only if the company stops considering me or is moving along with other candidates. Return “assessment_invite” or “assessment_confirmation” only if the email mentions an assessment. Return 'decision_update' only if the email is an offer to the position. Only return the category. Subject is " + subject + " and body is " + body
    response = model.generate_content(prompt)
    return True, response.text.strip()

def get_recipient(email: str) -> str:
    email = json.loads(email)
    recipient_email = email["recipient"]
    return recipient_email

def guess_domain(org_name: str, org_type: str) -> Tuple[bool, str]:
    prompt = (
            "I have an organization called '" + org_name + "', a '" + org_type + "'."
            "Please reply with exactly and only its primary website domain (for example, google.com or mit.edu)."
            "Do not include any protocol (`https://`), paths, or extra text."
    )
    response = model.generate_content(prompt)
    return True, response.text.strip().lower()