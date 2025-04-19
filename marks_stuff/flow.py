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

# ever get a separate email?

# choice?

# Internship Flow (actually build the flow)

def rejection_update_application(key: str) -> None:
    record = internship_applications.get(key)
    record["application"]["result"] = REJECT

def assessment_invite_update(key: str) -> None:
    record = internship_applications.get(key)
    record["application"]["result"]   = SUCCESS
    record["assessment"]["result"]    = IN_PROGRESS

def assessment_confirmation(key: str) -> None:
    record = internship_applications.get(key)
    record["assessment"]["confirmation"] = COMPLETE

def rejection_update_assessment(key: str) -> None:
    record = internship_applications.get(key)
    record["assessment"]["result"] = REJECT

def interview_invite_update(key: str) -> None:
    record = internship_applications.get(key)
    record["assessment"]["result"]   = SUCCESS
    record["interview"]["result"]   = IN_PROGRESS

def interview_confirmation(key: str) -> None:
    record = internship_applications.get(key)
    record["interview"]["confirmation"] = COMPLETE

def rejection_update_interview(key: str) -> None:
    record = internship_applications.get(key)
    record["interview"]["result"] = REJECT

def offer_update(key: str) -> None:
    record = internship_applications.get(key)
    record["interview"]["result"]   = SUCCESS
    record["offer"]["result"]   = SUCCESS
    record["offer"]["confirmation"] = COMPLETE

# Master's Programs Workflow

def rejection_update_application_masters(key: str) -> None:
    rec = masters_applications[key]
    rec["application"]["result"] = REJECT

def assessment_invite_update_masters(key: str) -> None:
    rec = masters_applications[key]
    rec["application"]["result"]   = SUCCESS
    rec["assessment"]["result"]    = IN_PROGRESS

def assessment_confirmation_masters(key: str) -> None:
    rec = masters_applications[key]
    rec["assessment"]["confirmation"] = COMPLETE


def rejection_update_assessment_masters(key: str) -> None:
    rec = masters_applications[key]
    rec["assessment"]["result"] = REJECT


def interview_invite_update_masters(key: str) -> None:
    rec = masters_applications[key]
    rec["assessment"]["result"] = SUCCESS
    rec["interview"]["result"]  = IN_PROGRESS


def interview_confirmation_masters(key: str) -> None:
    rec = masters_applications[key]
    rec["interview"]["confirmation"] = COMPLETE


def rejection_update_interview_masters(key: str) -> None:
    rec = masters_applications[key]
    rec["interview"]["result"] = REJECT


def decision_invite_update_masters(key: str) -> None:
    rec = masters_applications[key]
    rec["interview"]["result"]  = SUCCESS
    rec["decision"]["result"]   = IN_PROGRESS


def decision_confirmation_masters(key: str) -> None:
    rec = masters_applications[key]
    rec["decision"]["confirmation"] = COMPLETE


def acceptance_update_decision_masters(key: str) -> None:
    rec = masters_applications[key]
    rec["decision"]["result"] = SUCCESS


def rejection_update_decision_masters(key: str) -> None:
    rec = masters_applications[key]
    rec["decision"]["result"] = REJECT
