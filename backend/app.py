import base64
import json
from flask import Flask, request, jsonify

from database.workflow_final import final_workflow

app = Flask(__name__)

@app.route('/new-mail', methods=['POST'])
def api_endpoint():
    data = request.get_json()
    if not data:
        print(jsonify({"error": "No JSON data provided"}))
    if ('UNREAD' in data['labelIds']):
        sender = ''
        subject = ''
        date = ''
        text = ''
        for token in data['payload']['headers']:
            if token['name'] == 'From':
                sender = token['value']
            elif token['name'] == 'Subject':
                subject = token['value']
            elif token['name'] == 'Date':
                date = token['value']
        for part in data['payload']['parts']:
            if part.get("mimeType") == "text/plain":
                data = part.get("body", {}).get("data", "")
                decoded_bytes = base64.urlsafe_b64decode(data)
                decoded_text = decoded_bytes.decode("utf-8")
                text = decoded_text
        response = {
            'sender': sender,
            'subject': subject,
            'date': date,
            'text': text
        }
        final_workflow(json.dumps(response))
        return jsonify({"status": "success"})
    return jsonify({"status": "no data"})
    

@app.route('/new-mail', methods=['GET'])
def api_endpoint_get():
    return "New mail endpoint is running. "

if __name__ == '__main__':
     app.run(host="0.0.0.0", port=5000)