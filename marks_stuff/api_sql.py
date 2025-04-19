# api_server.py

import os
import sqlite3
import logging
from flask import Flask, g, jsonify, request
from flask_cors import CORS

# --- Configuration ---
class Config:
    DB_PATH = os.getenv("APPLICATIONS_DB_PATH", "applications.db")
    DEFAULT_LIMIT = 100
    MAX_LIMIT = 1000

# --- App Initialization ---
app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Setup basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Database Helpers ---
def get_db():
    """Get a SQLite connection for the current request context."""
    if "db" not in g:
        conn = sqlite3.connect(app.config["DB_PATH"])
        conn.row_factory = sqlite3.Row
        g.db = conn
    return g.db

@app.teardown_appcontext
def close_db(error):
    """Close the database at the end of the request."""
    db = g.pop("db", None)
    if db is not None:
        db.close()

def row_to_dict(row):
    """Convert a sqlite3.Row to a standard dict."""
    return {key: row[key] for key in row.keys()}

# --- Utility Functions ---
def parse_positive_int(param, default):
    """Parse a positive integer query parameter."""
    val = request.args.get(param, default)
    try:
        n = int(val)
        if n < 0:
            raise ValueError()
        return n, None
    except ValueError:
        return None, f"Invalid {param!r}: must be a non-negative integer"

# --- Health & Version Endpoints ---
@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="ok"), 200

@app.route("/version", methods=["GET"])
def version():
    return jsonify(version="1.0.0"), 200

# --- Dynamic Endpoint Factories ---
def list_endpoint(table, filters=None):
    def endpoint():
        db = get_db()
        # Pagination
        limit, err = parse_positive_int("limit", app.config["DEFAULT_LIMIT"])
        if err:
            return jsonify({"error": err}), 400
        offset, err = parse_positive_int("offset", 0)
        if err:
            return jsonify({"error": err}), 400
        limit = min(limit, app.config["MAX_LIMIT"])
        # Base query
        query = f"SELECT * FROM {table}"
        clauses, params = [], []
        # Optional filters
        if filters:
            for arg, col in filters.items():
                value = request.args.get(arg)
                if value:
                    clauses.append(f"{col} = ?")
                    params.append(value)
        if clauses:
            query += " WHERE " + " AND ".join(clauses)
        query += " LIMIT ? OFFSET ?"
        params.extend([limit, offset])
        rows = db.execute(query, params).fetchall()
        return jsonify([row_to_dict(r) for r in rows]), 200
    return endpoint

def get_endpoint(table):
    def endpoint(key):
        db = get_db()
        row = db.execute(f"SELECT * FROM {table} WHERE key = ?", (key,)).fetchone()
        if row is None:
            return jsonify({"error": f"{table} entry {key!r} not found"}), 404
        return jsonify(row_to_dict(row)), 200
    return endpoint

# --- Registering Routes ---
# Internships
app.add_url_rule(
    "/internships",
    "list_internships",
    list_endpoint("internships", filters={"status": "app_result", "company": "key"}),
    methods=["GET"]
)
app.add_url_rule(
    "/internships/<string:key>",
    "get_internship",
    get_endpoint("internships"),
    methods=["GET"]
)

# Masters
app.add_url_rule(
    "/masters",
    "list_masters",
    list_endpoint("masters", filters={"status": "app_result", "school": "key"}),
    methods=["GET"]
)
app.add_url_rule(
    "/masters/<string:key>",
    "get_master",
    get_endpoint("masters"),
    methods=["GET"]
)

# Scholarships
app.add_url_rule(
    "/scholarships",
    "list_scholarships",
    list_endpoint("scholarships", filters={"status": "app_result", "sponsor": "key"}),
    methods=["GET"]
)
app.add_url_rule(
    "/scholarships/<string:key>",
    "get_scholarship",
    get_endpoint("scholarships"),
    methods=["GET"]
)

# Clubs
app.add_url_rule(
    "/clubs",
    "list_clubs",
    list_endpoint("clubs", filters={"status": "app_result", "club": "key"}),
    methods=["GET"]
)
app.add_url_rule(
    "/clubs/<string:key>",
    "get_club",
    get_endpoint("clubs"),
    methods=["GET"]
)

# --- Run Server ---
if __name__ == "__main__":
    logger.info("Starting API server...")
    app.run(host="0.0.0.0", port=8000)