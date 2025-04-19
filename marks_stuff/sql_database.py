# 4 different tables approach

import sqlite3

DB_PATH = "applications.db"

def create_schema(db_path: str = DB_PATH) -> None:

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Internships table
    c.execute("""
    CREATE TABLE IF NOT EXISTS internships (
        key               TEXT PRIMARY KEY,
        app_conf          TEXT,
        app_result        TEXT,
        assess_conf       TEXT,
        assess_result     TEXT,
        interview_conf    TEXT,
        interview_result  TEXT,
        offer_conf        TEXT,
        offer_result      TEXT
    );
    """)

    # Master's Programs Table
    c.execute("""
    CREATE TABLE IF NOT EXISTS masters (
        key               TEXT PRIMARY KEY,
        app_conf          TEXT,
        app_result        TEXT,
        assess_conf       TEXT,
        assess_result     TEXT,
        interview_conf    TEXT,
        interview_result  TEXT,
        decision_conf     TEXT,
        decision_result   TEXT
    );
    """)

    # Scholarships table
    c.execute("""
    CREATE TABLE IF NOT EXISTS scholarships (
        key               TEXT PRIMARY KEY,
        app_conf          TEXT,
        app_result        TEXT,
        assess_conf       TEXT,
        assess_result     TEXT,
        interview_conf    TEXT,
        interview_result  TEXT,
        decision_conf     TEXT,
        decision_result   TEXT
    );
    """)

    # Clubs table
    c.execute("""
    CREATE TABLE IF NOT EXISTS clubs (
        key               TEXT PRIMARY KEY,
        app_conf          TEXT,
        app_result        TEXT,
        interview_conf    TEXT,
        interview_result  TEXT,
        decision_conf     TEXT,
        decision_result   TEXT
    );
    """)
    conn.commit()
    conn.close()


def persist_internships(apps: dict, db_path: str = DB_PATH) -> None:
    """
    Persist the internship_applications dict into the internships table.
    """
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for key, entry in apps.items():
        c.execute("""
            INSERT OR REPLACE INTO internships
                (key, app_conf, app_result,
                 assess_conf, assess_result,
                 interview_conf, interview_result,
                 offer_conf, offer_result)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            key,
            entry["application"]["confirmation"],
            entry["application"]["result"],
            entry["assessment"]["confirmation"],
            entry["assessment"]["result"],
            entry["interview"]["confirmation"],
            entry["interview"]["result"],
            entry["offer"]["confirmation"],
            entry["offer"]["result"],
        ))
    conn.commit()
    conn.close()


def persist_masters(apps: dict, db_path: str = DB_PATH) -> None:
    """
    Persist the masters_applications dict into the masters table.
    """
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for key, entry in apps.items():
        c.execute("""
            INSERT OR REPLACE INTO masters
                (key, app_conf, app_result,
                 assess_conf, assess_result,
                 interview_conf, interview_result,
                 decision_conf, decision_result)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            key,
            entry["application"]["confirmation"],
            entry["application"]["result"],
            entry["assessment"]["confirmation"],
            entry["assessment"]["result"],
            entry["interview"]["confirmation"],
            entry["interview"]["result"],
            entry["decision"]["confirmation"],
            entry["decision"]["result"],
        ))
    conn.commit()
    conn.close()


def persist_scholarships(apps: dict, db_path: str = DB_PATH) -> None:
    """
    Persist the scholar_applications dict into the scholarships table.
    """
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for key, entry in apps.items():
        materials = entry["application/materials"]
        c.execute("""
            INSERT OR REPLACE INTO scholarships
                (key, app_conf, app_result,
                 assess_conf, assess_result,
                 interview_conf, interview_result,
                 decision_conf, decision_result)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            key,
            materials["confirmation"],
            materials["result"],
            entry["assessment"]["confirmation"],
            entry["assessment"]["result"],
            entry["interview"]["confirmation"],
            entry["interview"]["result"],
            entry["decision"]["confirmation"],
            entry["decision"]["result"],
        ))
    conn.commit()
    conn.close()


def persist_clubs(apps: dict, db_path: str = DB_PATH) -> None:
    """
    Persist the club_applications dict into the clubs table.
    """
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for key, entry in apps.items():
        materials = entry["application/materials"]
        c.execute("""
            INSERT OR REPLACE INTO clubs
                (key, app_conf, app_result,
                 interview_conf, interview_result,
                 decision_conf, decision_result)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            key,
            materials["confirmation"],
            materials["result"],
            entry["interview"]["confirmation"],
            entry["interview"]["result"],
            entry["decision"]["confirmation"],
            entry["decision"]["result"],
        ))
    conn.commit()
    conn.close()

# database for each user, user_id