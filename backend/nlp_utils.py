import ndjson
from typing import Tuple
import requests

base_url = "http://localhost:11434"

def is_application(email: str) -> Tuple[bool, str]:
    print("Checking if email is application-related...")
    url = base_url+"/api/chat"
    payload = {
        "model": "gemma3:latest",
        "messages": [
            {
                "role": "user",
                "content": "Return 'True' if the following email is application related, and return 'False' otherwise: "+email
            }
        ]
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        result = ndjson.loads(response._content)
        response_text = ""
        for item in result:
            if item['message']['role'] == 'assistant':
                response_text = response_text+ item['message']['content']
        return True, response_text.strip()
    else:
        return False, response.status_code
    
def classify_email(email: str) -> Tuple[bool, str]:
    print("Classifying email...")
    url = base_url+"/api/chat"
    payload = {
        "model": "gemma3:latest",
        "messages": [
            {
                "role": "user",
                "content": "Categorize the email into one of the categories: 'confirmation', 'update' or 'other'. Only return the category: "+email
            }
        ]
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        result = ndjson.loads(response._content)
        response_text = ""
        for item in result:
            if item['message']['role'] == 'assistant':
                response_text = response_text+ item['message']['content']
        return True, response_text.strip()
    else:
        return False, response.status_code

def extract_info(email: str) -> Tuple[bool, list[str]]:
    print("Extracting information from email...")
    url = base_url+"/api/chat"
    payload = {
        "model": "gemma3:latest",
        "messages": [
            {
                "role": "user",
                "content": "Extract and return the company, position, date in format YYYYMMDD and result separated with comma. The result is 'Accepted' if it is a job offer, 'Action' if further action is required and 'Rejected' otherwise. The email is: "+email
            }
        ]
    
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        result = ndjson.loads(response._content)
        response_text = ""
        for item in result:
            if item['message']['role'] == 'assistant':
                response_text = response_text+ item['message']['content']
        return True, response_text.strip().split(",")
    else:
        return False, response.status_code
    
def classify_category(email: str) -> Tuple[bool, list[str]]:
    print("Classifying email category...")
    url = base_url+"/api/chat"
    payload = {
        "model": "gemma3:latest",
        "messages": [
            {
                "role": "user",
                "content": "Classify the email into one of the following categories: 'Internship', 'Club', 'Education', 'Scholarship', 'Other'. Return the category only. The email is: "+email
            }
        ]
    
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        result = ndjson.loads(response._content)
        response_text = ""
        for item in result:
            if item['message']['role'] == 'assistant':
                response_text = response_text+ item['message']['content']
        return True, response_text.strip()
    else:
        return False, response.status_code
    
def email_action(email: str) -> Tuple[bool, str]:
    print("Determining action type from email...")
    url = base_url+"/api/chat"
    payload = {
        "model": "gemma3:latest",
        "messages": [
            {
                "role": "user",
                "content": "Categorize the email into one of the following categories: “rejection”, “assessment_invite”, “assessment_confirmation”, “interview_invite”, “interview_confirmation”, “decision_update”. Only return the category. The email is: "+email
            }
        ]
    
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        result = ndjson.loads(response._content)
        response_text = ""
        for item in result:
            if item['message']['role'] == 'assistant':
                response_text = response_text+ item['message']['content']
        return True, response_text.strip()
    else:
        return False, response.status_code
    