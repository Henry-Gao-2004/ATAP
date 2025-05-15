# 4 different tables approach

import sqlite3
from datetime import datetime
from flask import session

DB_PATH = "C:\\User\\School\\2025_Spring\\CS329\ATAP\\backend\database\\applications.db"

def create_schema(db_path: str = DB_PATH) -> None:

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Users table
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id            INTEGER PRIMARY KEY AUTOINCREMENT,
        username      TEXT    UNIQUE     NOT NULL,
        password_hash TEXT                NOT NULL,
        created_at    TEXT    NOT NULL    DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Internships table
    c.execute("""
    CREATE TABLE IF NOT EXISTS internships (
        id               INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id          INTEGER NOT NULL REFERENCES users(id),
        key               TEXT    NOT NULL,
        app_conf          TEXT,
        app_result        TEXT,
        app_updated       TEXT,
        assess_conf       TEXT,
        assess_result     TEXT,
        assess_updated    TEXT,
        interview_conf    TEXT,
        interview_result  TEXT,
        interview_updated TEXT,
        offer_conf        TEXT,
        offer_result      TEXT,
        offer_updated     TEXT,
        UNIQUE(user_id, key)       
    );
    """)

    # Master's Programs Table
    c.execute("""
    CREATE TABLE IF NOT EXISTS masters (
        id               INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id          INTEGER NOT NULL REFERENCES users(id),
        key               TEXT    NOT NULL,
        app_conf          TEXT,
        app_result        TEXT,
        app_updated       TEXT,
        assess_conf       TEXT,
        assess_result     TEXT,
        assess_updated    TEXT,
        interview_conf    TEXT,
        interview_result  TEXT,
        interview_updated TEXT,
        decision_conf     TEXT,
        decision_result   TEXT,
        decision_updated  TEXT,
        UNIQUE(user_id, key) 
    );
    """)

    # Scholarships table
    c.execute("""
    CREATE TABLE IF NOT EXISTS scholarships (
        id               INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id          INTEGER NOT NULL REFERENCES users(id),
        key               TEXT    NOT NULL,
        app_conf          TEXT,
        app_result        TEXT,
        app_updated       TEXT,
        interview_conf    TEXT,
        interview_result  TEXT,
        interview_updated TEXT,
        decision_conf     TEXT,
        decision_result   TEXT,
        decision_updated  TEXT,
        UNIQUE(user_id, key) 
    );
    """)

    # Clubs table
    c.execute("""
    CREATE TABLE IF NOT EXISTS clubs (
        id               INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id          INTEGER NOT NULL REFERENCES users(id),
        key               TEXT    NOT NULL,
        app_conf          TEXT,
        app_result        TEXT,
        app_updated       TEXT,
        interview_conf    TEXT,
        interview_result  TEXT,
        interview_updated TEXT,
        offer_conf        TEXT,
        offer_result      TEXT,
        offer_updated     TEXT,
        UNIQUE(user_id, key)
    );
    """)
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def persist_internships(apps: dict, db_path: str = DB_PATH) -> None:
    create_schema(db_path)
    conn = get_db()
    c = conn.cursor()
    for key, entry in apps.items():
        c.execute("""
            INSERT OR REPLACE INTO internships
                (key, user_id, app_conf, app_result, app_updated,
                 assess_conf, assess_result, assess_updated,
                 interview_conf, interview_result, interview_updated,
                 offer_conf, offer_result, offer_updated)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            key,
            session['user_id'],
            entry["application"]["confirmation"],
            entry["application"]["result"],
            entry["application"].get("updated", datetime.now().isoformat()),
            entry["assessment"]["confirmation"],
            entry["assessment"]["result"],
            entry["assessment"].get("updated", datetime.now().isoformat()),
            entry["interview"]["confirmation"],
            entry["interview"]["result"],
            entry["interview"].get("updated", datetime.now().isoformat()),
            entry["offer"]["confirmation"],
            entry["offer"]["result"],
            entry["offer"].get("updated", datetime.now().isoformat())
        ))
    conn.commit()
    conn.close()

def persist_masters(apps: dict, db_path: str = DB_PATH) -> None:
    create_schema(db_path)
    conn = get_db()
    c = conn.cursor()
    for key, entry in apps.items():
        c.execute("""
            INSERT OR REPLACE INTO masters
                (key, user_id, app_conf, app_result, app_updated,
                 assess_conf, assess_result, assess_updated,
                 interview_conf, interview_result, interview_updated,
                 decision_conf, decision_result, decision_updated)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            key,
            session['user_id'],
            entry["application"]["confirmation"],
            entry["application"]["result"],
            entry["application"].get("updated", datetime.now().isoformat()),
            entry["assessment"]["confirmation"],
            entry["assessment"]["result"],
            entry["assessment"].get("updated", datetime.now().isoformat()),
            entry["interview"]["confirmation"],
            entry["interview"]["result"],
            entry["interview"].get("updated", datetime.now().isoformat()),
            entry["decision"]["confirmation"],
            entry["decision"]["result"],
            entry["decision"].get("updated", datetime.now().isoformat())
        ))
    conn.commit()
    conn.close()

def persist_scholarships(apps: dict, db_path: str = DB_PATH) -> None:
    create_schema(db_path)
    conn = get_db()
    c = conn.cursor()
    for key, entry in apps.items():
        c.execute("""
            INSERT OR REPLACE INTO scholarships
                (key, user_id, app_conf, app_result, app_updated,
                 interview_conf, interview_result, interview_updated,
                 decision_conf, decision_result, decision_updated)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            key,
            session['user_id'],
            entry["application"]["confirmation"],
            entry["application"]["result"],
            entry["application"].get("updated", datetime.now().isoformat()),
            entry["interview"]["confirmation"],
            entry["interview"]["result"],
            entry["interview"].get("updated", datetime.now().isoformat()),
            entry["decision"]["confirmation"],
            entry["decision"]["result"],
            entry["decision"].get("updated", datetime.now().isoformat())
        ))
    conn.commit()
    conn.close()

def persist_clubs(apps: dict, db_path: str = DB_PATH) -> None:
    create_schema(db_path)
    conn = get_db()
    c = conn.cursor()
    for key, entry in apps.items():
        c.execute("""
            INSERT OR REPLACE INTO clubs
                (key, user_id, app_conf, app_result, app_updated,
                 interview_conf, interview_result, interview_updated,
                 offer_conf, offer_result, offer_updated)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            key,
            session['user_id'],
            entry["application"]["confirmation"],
            entry["application"]["result"],
            entry["application"].get("updated", datetime.now().isoformat()),
            entry["interview"]["confirmation"],
            entry["interview"]["result"],
            entry["interview"].get("updated", datetime.now().isoformat()),
            entry["offer"]["confirmation"],
            entry["offer"]["result"],
            entry["offer"].get("updated", datetime.now().isoformat())
        ))
    conn.commit()
    conn.close()
