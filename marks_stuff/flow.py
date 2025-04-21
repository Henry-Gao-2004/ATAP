COMPLETE = 'complete'
INCOMPLETE = 'incomplete'

SUCCESS = 'success'
REJECT = 'reject'
IN_PROGRESS = 'in_progress'

NO_UPDATE = 'no_update'

# check if application-related email, get key (for accessing), then continue

# Doing linear flow (for now) (just from one to the next)
# Figure out non-linear flow ^^ (maybe not?)

# think about order (timestamp will be very important)
# rejection is unique (can't tell what step based on rejection)

# confirmation once completed interview? (assume that yes?)

# Cases accounted for (everything becomes green that is prior)
# 1. No assessment (straight interview)
# 2. No assessment or interview (scholarships)

# everything is flexible besides for getting initial email (non-negotiable)

from datetime import datetime

# Internship Flow

def rejection_update_application_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    record["application"]["result"] = REJECT
    record["application"]["updated"] = now

def assessment_invite_update_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    record["application"]["result"]   = SUCCESS
    record["application"]["updated"]  = now
    record["assessment"]["result"]    = IN_PROGRESS
    record["assessment"]["updated"]   = now

def assessment_confirmation_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["result"] = IN_PROGRESS
    record["assessment"]["updated"] = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

def rejection_update_assessment_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    record["assessment"]["result"] = REJECT
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

def interview_invite_update_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    record["assessment"]["result"]   = SUCCESS
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["interview"]["result"]   = IN_PROGRESS
    record["interview"]["updated"]  = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

def interview_confirmation_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["result"] = IN_PROGRESS
    record["interview"]["updated"] = now
    record["assessment"]["result"]   = SUCCESS
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["application"]["result"]   = SUCCESS
    record["application"]["updated"] = now

def rejection_update_interview_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    record["interview"]["result"] = REJECT
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["updated"] = now
    record["assessment"]["result"]   = SUCCESS
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["application"]["result"]   = SUCCESS
    record["application"]["updated"] = now

def offer_update_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    record["interview"]["result"]   = SUCCESS
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["updated"] = now
    record["offer"]["result"]   = SUCCESS
    record["offer"]["confirmation"] = COMPLETE
    record["offer"]["updated"] = now
    record["assessment"]["result"]   = SUCCESS
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

# Post-Grad Programs Workflow (later tackle management of all different steps of process)
# For now, just considering once application is done, every component of it is complete

def rejection_update_application_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    record["application"]["result"] = REJECT
    record["application"]["updated"] = now

def assessment_invite_update_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    record["application"]["result"]   = SUCCESS
    record["application"]["updated"]  = now
    record["assessment"]["result"]    = IN_PROGRESS
    record["assessment"]["updated"]   = now

def assessment_confirmation_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["result"] = IN_PROGRESS
    record["assessment"]["updated"] = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

def rejection_update_assessment_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    record["assessment"]["result"] = REJECT
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

def interview_invite_update_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    record["assessment"]["result"]   = SUCCESS
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["interview"]["result"]   = IN_PROGRESS
    record["interview"]["updated"]  = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

def interview_confirmation_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["result"] = IN_PROGRESS
    record["interview"]["updated"] = now
    record["assessment"]["result"]   = SUCCESS
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["application"]["result"]   = SUCCESS
    record["application"]["updated"] = now

def rejection_update_interview_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    record["interview"]["result"] = REJECT
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["updated"] = now
    record["assessment"]["result"]   = SUCCESS
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["application"]["result"]   = SUCCESS
    record["application"]["updated"] = now

def decision_update_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    record["interview"]["result"]   = SUCCESS
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["updated"] = now
    record["decision"]["result"]   = SUCCESS
    record["decision"]["confirmation"] = COMPLETE
    record["decision"]["updated"] = now
    record["assessment"]["result"]   = SUCCESS
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

# Scholarship Workflow

def rejection_update_application_schol(key: str) -> None:
    now = datetime.now().isoformat()
    record = scholar_applications.get(key)
    record["application"]["result"] = REJECT
    record["application"]["updated"] = now

def interview_invite_update_schol(key: str) -> None:
    now = datetime.now().isoformat()
    record = scholar_applications.get(key)
    record["interview"]["result"]   = IN_PROGRESS
    record["interview"]["updated"]  = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

def interview_confirmation_schol(key: str) -> None:
    now = datetime.now().isoformat()
    record = scholar_applications.get(key)
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["result"] = IN_PROGRESS
    record["interview"]["updated"] = now
    record["application"]["result"]   = SUCCESS
    record["application"]["updated"] = now

def rejection_update_interview_schol(key: str) -> None:
    now = datetime.now().isoformat()
    record = scholar_applications.get(key)
    record["interview"]["result"] = REJECT
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["updated"] = now
    record["application"]["result"]   = SUCCESS
    record["application"]["updated"] = now

def decision_update_schol(key: str) -> None:
    now = datetime.now().isoformat()
    record = scholar_applications.get(key)
    record["interview"]["result"]   = SUCCESS
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["updated"] = now
    record["decision"]["result"]   = SUCCESS
    record["decision"]["confirmation"] = COMPLETE
    record["decision"]["updated"] = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

# College Club Workflow

def rejection_update_application_club(key: str) -> None:
    now = datetime.now().isoformat()
    record = club_applications.get(key)
    record["application"]["result"] = REJECT
    record["application"]["updated"] = now

def interview_invite_update_club(key: str) -> None:
    now = datetime.now().isoformat()
    record = club_applications.get(key)
    record["interview"]["result"]   = IN_PROGRESS
    record["interview"]["updated"]  = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

def interview_confirmation_club(key: str) -> None:
    now = datetime.now().isoformat()
    record = club_applications.get(key)
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["result"]       = IN_PROGRESS
    record["interview"]["updated"from datetime import datetime # FIGURE THIS OUT!

# Internship Flow

def rejection_update_application_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    record["application"]["result"] = REJECT
    record["application"]["updated"] = now

def assessment_invite_update_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    record["application"]["result"]   = SUCCESS
    record["application"]["updated"]  = now
    record["assessment"]["result"]    = IN_PROGRESS
    record["assessment"]["updated"]   = now

def assessment_confirmation_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["result"] = IN_PROGRESS
    record["assessment"]["updated"] = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

def rejection_update_assessment_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    record["assessment"]["result"] = REJECT
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

def interview_invite_update_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    record["assessment"]["result"]   = SUCCESS
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["interview"]["result"]   = IN_PROGRESS
    record["interview"]["updated"]  = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

def interview_confirmation_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["result"] = IN_PROGRESS
    record["interview"]["updated"] = now
    record["assessment"]["result"]   = SUCCESS
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["application"]["result"]   = SUCCESS
    record["application"]["updated"] = now

def rejection_update_interview_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    record["interview"]["result"] = REJECT
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["updated"] = now
    record["assessment"]["result"]   = SUCCESS
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["application"]["result"]   = SUCCESS
    record["application"]["updated"] = now

def offer_update_int(key: str) -> None:
    now = datetime.now().isoformat()
    record = internship_applications.get(key)
    record["interview"]["result"]   = SUCCESS
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["updated"] = now
    record["offer"]["result"]   = SUCCESS
    record["offer"]["confirmation"] = COMPLETE
    record["offer"]["updated"] = now
    record["assessment"]["result"]   = SUCCESS
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

# Post-Grad Programs Workflow (later tackle management of all different steps of process)
# For now, just considering once application is done, every component of it is complete

def rejection_update_application_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    record["application"]["result"] = REJECT
    record["application"]["updated"] = now

def assessment_invite_update_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    record["application"]["result"]   = SUCCESS
    record["application"]["updated"]  = now
    record["assessment"]["result"]    = IN_PROGRESS
    record["assessment"]["updated"]   = now

def assessment_confirmation_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["result"] = IN_PROGRESS
    record["assessment"]["updated"] = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

def rejection_update_assessment_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    record["assessment"]["result"] = REJECT
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

def interview_invite_update_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    record["assessment"]["result"]   = SUCCESS
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["interview"]["result"]   = IN_PROGRESS
    record["interview"]["updated"]  = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

def interview_confirmation_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["result"] = IN_PROGRESS
    record["interview"]["updated"] = now
    record["assessment"]["result"]   = SUCCESS
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["application"]["result"]   = SUCCESS
    record["application"]["updated"] = now

def rejection_update_interview_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    record["interview"]["result"] = REJECT
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["updated"] = now
    record["assessment"]["result"]   = SUCCESS
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["application"]["result"]   = SUCCESS
    record["application"]["updated"] = now

def decision_update_post(key: str) -> None:
    now = datetime.now().isoformat()
    record = masters_applications.get(key)
    record["interview"]["result"]   = SUCCESS
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["updated"] = now
    record["decision"]["result"]   = SUCCESS
    record["decision"]["confirmation"] = COMPLETE
    record["decision"]["updated"] = now
    record["assessment"]["result"]   = SUCCESS
    record["assessment"]["confirmation"] = COMPLETE
    record["assessment"]["updated"] = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

# Scholarship Workflow

def rejection_update_application_schol(key: str) -> None:
    now = datetime.now().isoformat()
    record = scholar_applications.get(key)
    record["application"]["result"] = REJECT
    record["application"]["updated"] = now

def interview_invite_update_schol(key: str) -> None:
    now = datetime.now().isoformat()
    record = scholar_applications.get(key)
    record["interview"]["result"]   = IN_PROGRESS
    record["interview"]["updated"]  = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

def interview_confirmation_schol(key: str) -> None:
    now = datetime.now().isoformat()
    record = scholar_applications.get(key)
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["result"] = IN_PROGRESS
    record["interview"]["updated"] = now
    record["application"]["result"]   = SUCCESS
    record["application"]["updated"] = now

def rejection_update_interview_schol(key: str) -> None:
    now = datetime.now().isoformat()
    record = scholar_applications.get(key)
    record["interview"]["result"] = REJECT
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["updated"] = now
    record["application"]["result"]   = SUCCESS
    record["application"]["updated"] = now

def decision_update_schol(key: str) -> None:
    now = datetime.now().isoformat()
    record = scholar_applications.get(key)
    record["interview"]["result"]   = SUCCESS
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["updated"] = now
    record["decision"]["result"]   = SUCCESS
    record["decision"]["confirmation"] = COMPLETE
    record["decision"]["updated"] = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

# College Club Workflow

def rejection_update_application_club(key: str) -> None:
    now = datetime.now().isoformat()
    record = club_applications.get(key)
    record["application"]["result"] = REJECT
    record["application"]["updated"] = now

def interview_invite_update_club(key: str) -> None:
    now = datetime.now().isoformat()
    record = club_applications.get(key)
    record["interview"]["result"]   = IN_PROGRESS
    record["interview"]["updated"]  = now
    record["application"]["result"] = SUCCESS
    record["application"]["updated"] = now

def interview_confirmation_club(key: str) -> None:
    now = datetime.now().isoformat()
    record = club_applications.get(key)
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["result"]       = IN_PROGRESS
    record["interview"]["updated"]      = now
    record["application"]["result"]     = SUCCESS
    record["application"]["updated"]    = now

def rejection_update_interview_club(key: str) -> None:
    now = datetime.now().isoformat()
    record = club_applications.get(key)
    record["interview"]["result"]       = REJECT
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["updated"]      = now
    record["application"]["result"]     = SUCCESS
    record["application"]["updated"]    = now

def offer_update_club(key: str) -> None:
    now = datetime.now().isoformat()
    record = club_applications.get(key)
    record["interview"]["result"]       = SUCCESS
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["updated"]      = now
    record["offer"]["result"]           = SUCCESS
    record["offer"]["confirmation"]     = COMPLETE
    record["offer"]["updated"]          = now
    record["application"]["result"]     = SUCCESS
    record["application"]["updated"]    = now
]      = now
    record["application"]["result"]     = SUCCESS
    record["application"]["updated"]    = now

def rejection_update_interview_club(key: str) -> None:
    now = datetime.now().isoformat()
    record = club_applications.get(key)
    record["interview"]["result"]       = REJECT
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["updated"]      = now
    record["application"]["result"]     = SUCCESS
    record["application"]["updated"]    = now

def offer_update_club(key: str) -> None:
    now = datetime.now().isoformat()
    record = club_applications.get(key)
    record["interview"]["result"]       = SUCCESS
    record["interview"]["confirmation"] = COMPLETE
    record["interview"]["updated"]      = now
    record["offer"]["result"]           = SUCCESS
    record["offer"]["confirmation"]     = COMPLETE
    record["offer"]["updated"]          = now
    record["application"]["result"]     = SUCCESS
    record["application"]["updated"]    = now
