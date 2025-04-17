import base64
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/new-mail', methods=['POST'])
def api_endpoint():
    data = request.get_json()
    if not data:
        print(jsonify({"error": "No JSON data provided"}))
    if ('UNREAD' in data['labelIds']):
        sender = ''
        subject = ''
        text = ''
        for token in data['payload']['headers']:
            if token['name'] == 'From':
                sender = token['value']
            elif token['name'] == 'Subject':
                subject = token['value']
        for part in data['payload']['parts']:
            if part.get("mimeType") == "text/plain":
                data = part.get("body", {}).get("data", "")
                decoded_bytes = base64.urlsafe_b64decode(data)
                decoded_text = decoded_bytes.decode("utf-8")
                text = decoded_text
        print("Sender:"+sender+" Subject:"+subject+" Text:"+text)
        return jsonify({"status": "success"})
    return jsonify({"status": "no data"})
    

@app.route('/new-mail', methods=['GET'])
def api_endpoint_get():
    return "New mail endpoint is running. "

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)