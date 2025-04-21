# closed dot = completed ;  open dot = not completed
# green = success; orange = in progress; red = rejected; white = no_update

# Creating global dictionaries
internship_applications = dict()
masters_applications = dict()  # fix to post_grad later
scholar_applications = dict()
club_applications = dict()

from datetime import datetime

# Tags

INTERNSHIP = 'internship'
POST_GRAD = 'post_grad'
SCHOLARSHIP = 'scholarship'
CLUB = 'club'

COMPLETE = 'complete'
INCOMPLETE = 'incomplete'

SUCCESS = 'success' # green
REJECT = 'reject' # red / maroon
IN_PROGRESS = 'in_progress' # orange

NO_UPDATE = 'no_update' # white

# Internships

def internship_insert(key: str) -> None:
    now = datetime.now().isoformat()
    entry = {
        "application": {
            "confirmation": COMPLETE,
            "result": IN_PROGRESS,
            "updated": now
        },
        "assessment": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE,
            "updated": now
        },
        "interview": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE,
            "updated": now
        },
        "offer": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE,
            "updated": now
        },
    }

    internship_applications[key] = entry

# Master's Programs

def masters_insert(key: str) -> None:
    now = datetime.now().isoformat()
    entry = {
        "application": {
            "confirmation": COMPLETE,
            "result": IN_PROGRESS,
            "updated": now
        },
        "assessment": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE,
            "updated": now
        },
        "interview": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE,
            "updated": now
        },
        "decision": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE,
            "updated": now
        },
    }

    masters_applications[key] = entry

# Scholarships (keep in mind that definition of assessment varies with application type)

def scholar_insert(key: str) -> None:
    now = datetime.now().isoformat()
    entry = {
        "application": {
            "confirmation": COMPLETE,
            "result": IN_PROGRESS,
            "updated": now
        },
        "interview": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE,
            "updated": now
        },
        "decision": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE,
            "updated": now
        },
    }

    scholar_applications[key] = entry

# Clubs (keep in mind that definition of assessment varies with application type)

def club_insert(key: str) -> None:
    now = datetime.now().isoformat()
    entry = {
        "application": {
            "confirmation": COMPLETE,
            "result": IN_PROGRESS,
            "updated": now
        },
        "interview": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE,
            "updated": now
        },
        "offer": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE,
            "updated": now
        },
    }

    club_applications[key] = entry


