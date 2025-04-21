# criteria for a task: INCOMPLETE and IN_PROGRESS

# make the date nice

import sqlite3
from datetime import datetime

DB_PATH = "applications.db"

def extract_tasks(db_path: str = DB_PATH) -> list:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    tables = {
        "internships": ["assessment", "interview", "offer"],
        "masters": ["assessment", "interview", "decision"],
        "scholarships": ["interview", "decision"],
        "clubs": ["interview", "offer"]
    }

    task_list = []

    for table, stages in tables.items():
        rows = c.execute(f"SELECT * FROM {table}").fetchall()
        col_names = [desc[0] for desc in c.description]

        for row in rows:
            row_dict = dict(zip(col_names, row))
            app_key = row_dict["key"]

            for stage in stages:
                conf = row_dict.get(f"{stage}_conf", "")
                res = row_dict.get(f"{stage}_result", "")
                updated = row_dict.get(f"{stage}_updated", "")
                if conf == "incomplete" and res == "in_progress":
                    task_list.append({
                        "application": app_key,
                        "stage": stage,
                        "last_updated": updated,
                        "source_table": table
                    })

    conn.close()

    # Sort tasks by most recent update time (descending)
    task_list.sort(key=lambda t: t["last_updated"], reverse=True)
    return task_list

