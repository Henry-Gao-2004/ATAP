# 4 different tables approach

import sqlite3
from datetime import datetime

DB_PATH = "C:\\User\\School\\2025_Spring\\CS329\ATAP\\backend\database\\applications.db"

def create_schema(db_path: str = DB_PATH) -> None:

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Internships table
    c.execute("""
    CREATE TABLE IF NOT EXISTS internships (
        key               TEXT PRIMARY KEY,
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
        offer_updated     TEXT
    );
    """)

    # Master's Programs Table
    c.execute("""
    CREATE TABLE IF NOT EXISTS masters (
        key               TEXT PRIMARY KEY,
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
        decision_updated  TEXT
    );
    """)

    # Scholarships table
    c.execute("""
    CREATE TABLE IF NOT EXISTS scholarships (
        key               TEXT PRIMARY KEY,
        app_conf          TEXT,
        app_result        TEXT,
        app_updated       TEXT,
        interview_conf    TEXT,
        interview_result  TEXT,
        interview_updated TEXT,
        decision_conf     TEXT,
        decision_result   TEXT,
        decision_updated  TEXT
    );
    """)

    # Clubs table
    c.execute("""
    CREATE TABLE IF NOT EXISTS clubs (
        key               TEXT PRIMARY KEY,
        app_conf          TEXT,
        app_result        TEXT,
        app_updated       TEXT,
        interview_conf    TEXT,
        interview_result  TEXT,
        interview_updated TEXT,
        offer_conf        TEXT,
        offer_result      TEXT,
        offer_updated     TEXT
    );
    """)
    conn.commit()
    conn.close()

def persist_internships(apps: dict, db_path: str = DB_PATH) -> None:
    create_schema(db_path)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for key, entry in apps.items():
        c.execute("""
            INSERT OR REPLACE INTO internships
                (key, app_conf, app_result, app_updated,
                 assess_conf, assess_result, assess_updated,
                 interview_conf, interview_result, interview_updated,
                 offer_conf, offer_result, offer_updated)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            key,
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
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for key, entry in apps.items():
        c.execute("""
            INSERT OR REPLACE INTO masters
                (key, app_conf, app_result, app_updated,
                 assess_conf, assess_result, assess_updated,
                 interview_conf, interview_result, interview_updated,
                 decision_conf, decision_result, decision_updated)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            key,
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
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for key, entry in apps.items():
        c.execute("""
            INSERT OR REPLACE INTO scholarships
                (key, app_conf, app_result, app_updated,
                 interview_conf, interview_result, interview_updated,
                 decision_conf, decision_result, decision_updated)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            key,
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
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for key, entry in apps.items():
        c.execute("""
            INSERT OR REPLACE INTO clubs
                (key, app_conf, app_result, app_updated,
                 interview_conf, interview_result, interview_updated,
                 offer_conf, offer_result, offer_updated)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            key,
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
