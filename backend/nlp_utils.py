import ndjson
from typing import Tuple
import requests

def is_application(email: str) -> Tuple[bool, str]:
    url = "http://localhost:11434/api/chat"
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
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "gemma3:latest",
        "messages": [
            {
                "role": "user",
                "content": "Categorize the email into category 'comfirmation', 'update' or 'other'. Only return the category: "+email
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
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "gemma3:latest",
        "messages": [
            {
                "role": "user",
                "content": "Extract and print the company, position and result separated with comma. The result is 'Accepted' if it is a job offer and 'Rejected' otherwise. The email is: "+email
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