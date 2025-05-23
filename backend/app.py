import os
import base64
import json
import requests
from pathlib import Path
from flask import Flask, request, jsonify, send_file, abort
from dotenv import load_dotenv

from database.workflow_final import final_workflow

app = Flask(__name__)

# ─── Logo.dev proxy setup ────────────────────────────────────────────────────

# 1) Load your LOGO_DEV_TOKEN from the project‑root .env
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

# 2) Ensure the disk cache directory exists
LOGO_CACHE = os.path.join(os.path.dirname(__file__), "static", "logos")
os.makedirs(LOGO_CACHE, exist_ok=True)


def _cached_svg_response(path):
    """
    Wrap send_file with 1‑year HTTP caching headers.
    """
    from datetime import datetime, timedelta
    from flask import make_response

    resp = make_response(send_file(path, mimetype="image/svg+xml"))
    # 365 days in seconds
    max_age = 31536000
    resp.headers["Cache-Control"] = f"public, max-age={max_age}"
    expires = datetime.utcnow() + timedelta(seconds=max_age)
    resp.headers["Expires"] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
    return resp


@app.route("/logo/<path:domain>.svg")
def logo_proxy(domain):
    """
    1) If we have static/logos/<domain>.svg on disk, serve it with a 1‑year cache.
    2) Otherwise fetch from logo.dev, save it, then serve with the same cache headers.
    """
    local_path = os.path.join(LOGO_CACHE, f"{domain}.svg")

    # Serve from disk if cached
    if os.path.exists(local_path):
        return _cached_svg_response(local_path)

    # Fetch from logo.dev
    token = os.getenv("LOGO_DEV_TOKEN")
    if not token:
        abort(500, "Missing LOGO_DEV_TOKEN in environment")

    url = f"https://img.logo.dev/{domain}.svg?token={token}"
    resp = requests.get(url, timeout=5)
    if resp.status_code != 200:
        abort(404)

    # Save and serve
    with open(local_path, "wb") as f:
        f.write(resp.content)

    return _cached_svg_response(local_path)


def deconstruct_parts(data):
    text = ""
    if "body" in data:
        encoded_text = data["body"].get("data", "")
        decoded_bytes = base64.urlsafe_b64decode(encoded_text + '==')
        decoded_text = decoded_bytes.decode('utf-8')
        text += decoded_text
    if "parts" in data:
        for part in data['parts']:
            text += deconstruct_parts(part)
    return text


@app.route('/new-mail', methods=['POST'])
def api_endpoint():
    data = request.get_json()
    if not data:
        print(jsonify({"error": "No JSON data provided"}))
    if 'labelIds' in data and 'UNREAD' in data['labelIds']:
        sender = ''
        recipient = ''
        date = ''
        print(data['payload']['headers'])
        for token in data['payload']['headers']:
            if token['name'] == 'From':
                sender = token['value']
            elif token['name'] == 'To':
                recipient = token['value']
            elif token['name'] == 'Subject':
                subject = token['value']
            elif token['name'] == 'Date':
                date = token['value']
        text = deconstruct_parts(data["payload"])

        response = {
            'sender': sender,
            'recipient': recipient,
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