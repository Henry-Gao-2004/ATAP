from flask import Flask, redirect, request
import requests
import os
from urllib.parse import urlencode

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Replace with your credentials
GOOGLE_CLIENT_ID = "3308161800-pm4bohp89b6sn43dslaf40jkkmf35vvs.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
REDIRECT_URI = "http://localhost:5001/callback"
SCOPE = "openid email"

# Fetch the discovery document
DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
discovery_doc = requests.get(DISCOVERY_URL).json()

AUTH_URI = discovery_doc["authorization_endpoint"]
TOKEN_URI = discovery_doc["token_endpoint"]
USERINFO_URI = discovery_doc["userinfo_endpoint"]

@app.route("/")
def index():
    return '<a href="/login">Login with Google</a>'

@app.route("/login")
def login():
    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": SCOPE,
        "access_type": "offline",
        "prompt": "consent"
    }
    return redirect(f"{AUTH_URI}?{urlencode(params)}")

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return "Missing code", 400

    # Exchange code for access token
    token_data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    token_resp = requests.post(TOKEN_URI, data=token_data)
    token_json = token_resp.json()
    access_token = token_json.get("access_token")

    if not access_token:
        return "Token exchange failed", 400

    # Fetch user info using access token
    headers = {"Authorization": f"Bearer {access_token}"}
    userinfo_resp = requests.get(USERINFO_URI, headers=headers)
    userinfo = userinfo_resp.json()
    email = userinfo.get("email")

    if not email:
        return "Failed to retrieve email", 400

    # Redirect to localhost:5001 with email as query param
    return redirect(f"http://localhost:5001?email={email}")

if __name__ == "__main__":
    app.run(port=5001, debug=True)
