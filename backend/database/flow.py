from database.type_dicts import *

COMPLETE = 'complete'
INCOMPLETE = 'incomplete'

SUCCESS = 'success'
REJECT = 'reject'
IN_PROGRESS = 'in_progress'

NO_UPDATE = 'no_update'

from datetime import datetime

# Internship Flow

def rejection_update_application_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    if record["application"]["result"] != REJECT:
        record["application"]["result"] = REJECT
        record["application"]["updated"] = now

def assessment_invite_update_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now
    if record["assessment"]["result"] != IN_PROGRESS:
        record["assessment"]["result"] = IN_PROGRESS
        record["assessment"]["updated"] = now

def assessment_confirmation_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    if record["assessment"]["confirmation"] != COMPLETE:
        record["assessment"]["confirmation"] = COMPLETE
        record["assessment"]["updated"] = now
    if record["assessment"]["result"] != IN_PROGRESS:
        record["assessment"]["result"] = IN_PROGRESS
        record["assessment"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

def rejection_update_assessment_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    if record["assessment"]["result"] != REJECT:
        record["assessment"]["result"] = REJECT
        record["assessment"]["updated"] = now
    if record["assessment"]["confirmation"] != COMPLETE:
        record["assessment"]["confirmation"] = COMPLETE
        record["assessment"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

def interview_invite_update_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    if record["assessment"]["result"] != SUCCESS:
        record["assessment"]["result"] = SUCCESS
        record["assessment"]["updated"] = now
    if record["assessment"]["confirmation"] != COMPLETE:
        record["assessment"]["confirmation"] = COMPLETE
        record["assessment"]["updated"] = now
    if record["interview"]["result"] != IN_PROGRESS:
        record["interview"]["result"] = IN_PROGRESS
        record["interview"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

def interview_confirmation_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    if record["interview"]["confirmation"] != COMPLETE:
        record["interview"]["confirmation"] = COMPLETE
        record["interview"]["updated"] = now
    if record["interview"]["result"] != IN_PROGRESS:
        record["interview"]["result"] = IN_PROGRESS
        record["interview"]["updated"] = now
    if record["assessment"]["result"] != SUCCESS:
        record["assessment"]["result"] = SUCCESS
        record["assessment"]["updated"] = now
    if record["assessment"]["confirmation"] != COMPLETE:
        record["assessment"]["confirmation"] = COMPLETE
        record["assessment"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

def rejection_update_interview_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    if record["interview"]["result"] != REJECT:
        record["interview"]["result"] = REJECT
        record["interview"]["updated"] = now
    if record["interview"]["confirmation"] != COMPLETE:
        record["interview"]["confirmation"] = COMPLETE
        record["interview"]["updated"] = now
    if record["assessment"]["result"] != SUCCESS:
        record["assessment"]["result"] = SUCCESS
        record["assessment"]["updated"] = now
    if record["assessment"]["confirmation"] != COMPLETE:
        record["assessment"]["confirmation"] = COMPLETE
        record["assessment"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

def offer_update_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    if record["interview"]["result"] != SUCCESS:
        record["interview"]["result"] = SUCCESS
        record["interview"]["updated"] = now
    if record["interview"]["confirmation"] != COMPLETE:
        record["interview"]["confirmation"] = COMPLETE
        record["interview"]["updated"] = now
    if record["offer"]["result"] != SUCCESS:
        record["offer"]["result"] = SUCCESS
        record["offer"]["updated"] = now
    if record["offer"]["confirmation"] != COMPLETE:
        record["offer"]["confirmation"] = COMPLETE
        record["offer"]["updated"] = now
    if record["assessment"]["result"] != SUCCESS:
        record["assessment"]["result"] = SUCCESS
        record["assessment"]["updated"] = now
    if record["assessment"]["confirmation"] != COMPLETE:
        record["assessment"]["confirmation"] = COMPLETE
        record["assessment"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

# Post-Grad Programs Workflow (later tackle management of all different steps of process)
# For now, just considering once application is done, every component of it is complete

def rejection_update_application_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    if record["application"]["result"] != REJECT:
        record["application"]["result"] = REJECT
        record["application"]["updated"] = now

def assessment_invite_update_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now
    if record["assessment"]["result"] != IN_PROGRESS:
        record["assessment"]["result"] = IN_PROGRESS
        record["assessment"]["updated"] = now

def assessment_confirmation_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    if record["assessment"]["confirmation"] != COMPLETE:
        record["assessment"]["confirmation"] = COMPLETE
        record["assessment"]["updated"] = now
    if record["assessment"]["result"] != IN_PROGRESS:
        record["assessment"]["result"] = IN_PROGRESS
        record["assessment"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

def rejection_update_assessment_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    if record["assessment"]["result"] != REJECT:
        record["assessment"]["result"] = REJECT
        record["assessment"]["updated"] = now
    if record["assessment"]["confirmation"] != COMPLETE:
        record["assessment"]["confirmation"] = COMPLETE
        record["assessment"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

def interview_invite_update_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    if record["assessment"]["result"] != SUCCESS:
        record["assessment"]["result"] = SUCCESS
        record["assessment"]["updated"] = now
    if record["assessment"]["confirmation"] != COMPLETE:
        record["assessment"]["confirmation"] = COMPLETE
        record["assessment"]["updated"] = now
    if record["interview"]["result"] != IN_PROGRESS:
        record["interview"]["result"] = IN_PROGRESS
        record["interview"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

def interview_confirmation_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    if record["interview"]["confirmation"] != COMPLETE:
        record["interview"]["confirmation"] = COMPLETE
        record["interview"]["updated"] = now
    if record["interview"]["result"] != IN_PROGRESS:
        record["interview"]["result"] = IN_PROGRESS
        record["interview"]["updated"] = now
    if record["assessment"]["result"] != SUCCESS:
        record["assessment"]["result"] = SUCCESS
        record["assessment"]["updated"] = now
    if record["assessment"]["confirmation"] != COMPLETE:
        record["assessment"]["confirmation"] = COMPLETE
        record["assessment"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

def rejection_update_interview_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    if record["interview"]["result"] != REJECT:
        record["interview"]["result"] = REJECT
        record["interview"]["updated"] = now
    if record["interview"]["confirmation"] != COMPLETE:
        record["interview"]["confirmation"] = COMPLETE
        record["interview"]["updated"] = now
    if record["assessment"]["result"] != SUCCESS:
        record["assessment"]["result"] = SUCCESS
        record["assessment"]["updated"] = now
    if record["assessment"]["confirmation"] != COMPLETE:
        record["assessment"]["confirmation"] = COMPLETE
        record["assessment"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

def decision_update_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    if record["interview"]["result"] != SUCCESS:
        record["interview"]["result"] = SUCCESS
        record["interview"]["updated"] = now
    if record["interview"]["confirmation"] != COMPLETE:
        record["interview"]["confirmation"] = COMPLETE
        record["interview"]["updated"] = now
    if record["decision"]["result"] != SUCCESS:
        record["decision"]["result"] = SUCCESS
        record["decision"]["updated"] = now
    if record["decision"]["confirmation"] != COMPLETE:
        record["decision"]["confirmation"] = COMPLETE
        record["decision"]["updated"] = now
    if record["assessment"]["result"] != SUCCESS:
        record["assessment"]["result"] = SUCCESS
        record["assessment"]["updated"] = now
    if record["assessment"]["confirmation"] != COMPLETE:
        record["assessment"]["confirmation"] = COMPLETE
        record["assessment"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

# Scholarship Workflow

def rejection_update_application_schol(key: str) -> None:
    now = datetime.now().isoformat()
    record = scholar_applications.get(key)
    if record["application"]["result"] != REJECT:
        record["application"]["result"] = REJECT
        record["application"]["updated"] = now

def interview_invite_update_schol(key: str) -> None:
    now = datetime.now().isoformat()
    record = scholar_applications.get(key)
    if record["interview"]["result"] != IN_PROGRESS:
        record["interview"]["result"] = IN_PROGRESS
        record["interview"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

def interview_confirmation_schol(key: str) -> None:
    now = datetime.now().isoformat()
    record = scholar_applications.get(key)
    if record["interview"]["confirmation"] != COMPLETE:
        record["interview"]["confirmation"] = COMPLETE
        record["interview"]["updated"] = now
    if record["interview"]["result"] != IN_PROGRESS:
        record["interview"]["result"] = IN_PROGRESS
        record["interview"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

def rejection_update_interview_schol(key: str) -> None:
    now = datetime.now().isoformat()
    record = scholar_applications.get(key)
    if record["interview"]["result"] != REJECT:
        record["interview"]["result"] = REJECT
        record["interview"]["updated"] = now
    if record["interview"]["confirmation"] != COMPLETE:
        record["interview"]["confirmation"] = COMPLETE
        record["interview"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

def decision_update_schol(key: str) -> None:
    now = datetime.now().isoformat()
    record = scholar_applications.get(key)
    if record["interview"]["result"] != SUCCESS:
        record["interview"]["result"] = SUCCESS
        record["interview"]["updated"] = now
    if record["interview"]["confirmation"] != COMPLETE:
        record["interview"]["confirmation"] = COMPLETE
        record["interview"]["updated"] = now
    if record["decision"]["result"] != SUCCESS:
        record["decision"]["result"] = SUCCESS
        record["decision"]["updated"] = now
    if record["decision"]["confirmation"] != COMPLETE:
        record["decision"]["confirmation"] = COMPLETE
        record["decision"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

# College Club Workflow

def rejection_update_application_club(key: str) -> None:
    now = datetime.now().isoformat()
    record = club_applications.get(key)
    if record["application"]["result"] != REJECT:
        record["application"]["result"] = REJECT
        record["application"]["updated"] = now

def interview_invite_update_club(key: str) -> None:
    now = datetime.now().isoformat()
    record = club_applications.get(key)
    if record["interview"]["result"] != IN_PROGRESS:
        record["interview"]["result"] = IN_PROGRESS
        record["interview"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

def interview_confirmation_club(key: str) -> None:
    now = datetime.now().isoformat()
    record = club_applications.get(key)
    if record["interview"]["confirmation"] != COMPLETE:
        record["interview"]["confirmation"] = COMPLETE
        record["interview"]["updated"] = now
    if record["interview"]["result"] != IN_PROGRESS:
        record["interview"]["result"] = IN_PROGRESS
        record["interview"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

def rejection_update_interview_club(key: str) -> None:
    now = datetime.now().isoformat()
    record = club_applications.get(key)
    if record["interview"]["result"] != REJECT:
        record["interview"]["result"] = REJECT
        record["interview"]["updated"] = now
    if record["interview"]["confirmation"] != COMPLETE:
        record["interview"]["confirmation"] = COMPLETE
        record["interview"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now

def offer_update_club(key: str) -> None:
    now = datetime.now().isoformat()
    record = club_applications.get(key)
    if record["interview"]["result"] != SUCCESS:
        record["interview"]["result"] = SUCCESS
        record["interview"]["updated"] = now
    if record["interview"]["confirmation"] != COMPLETE:
        record["interview"]["confirmation"] = COMPLETE
        record["interview"]["updated"] = now
    if record["offer"]["result"] != SUCCESS:
        record["offer"]["result"] = SUCCESS
        record["offer"]["updated"] = now
    if record["offer"]["confirmation"] != COMPLETE:
        record["offer"]["confirmation"] = COMPLETE
        record["offer"]["updated"] = now
    if record["application"]["result"] != SUCCESS:
        record["application"]["result"] = SUCCESS
        record["application"]["updated"] = now
