# closed dot = completed ;  open dot = not completed
# green = success; orange = in progress; red = rejected

# assume a demo without multiple potential for multiple interviews (and having an assessment, then interview, can make better later for complexity-sake)

# for every application, mantain this information (tags should be generated right away)

# once apply, should be dot (completed) and orange (don't know)

# don't need application confirmation bc that's already one by if the email is an app. confirmation

# steps for assessment and interview should be recieve it, complete it, await decision

# connect to a database of a ton of photos (company/grad school logos)

# Do separate nested dictionaries for each type of application

# Expand from uniform (static to dynamic)

# Confirmation controls open/closed dot

# do separate methods for detecting if interview or assessment
# trigger orange, open dot

# DELETE AFTER 12 MONTHS (or somehow make applications unique)

APPLICATION_CONFIRMATION = True # permanently True bc that is how detected
APPLICATION_RESULT = False

ASSESSMENT_CONFIRMATION = False
ASSESSMENT_RESULT = False

INTERVIEW_CONFIRMATION = False
INTERVIEW_RESULT = False

OFFER_RESULT = False  # if successful interview = offer
# still include bc might not be like passed interview, just straight to offer
# backwards logic


# Figure out how to do insertions based on assessment/interview
# from extract_info?? ^^

# think about what to add to each individual

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

# Email Category Classifier

# Henry already made

# Internships (run if email is detected to be an internship)

# API for use of methods

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

# clubs would be weird (not usually a confirmation, but more like a rejection, would have to adjust workflow for clubs)
# Clubs (keep in mind that definition of assessment varies with application type)

def club_insert(key: str) -> None:
    now = datetime.now().isoformat()
    entry = {
        "application": {
            "confirmation": COMPLETE,
            "result": IN_PROGRESS, # will get updated when get either accepted/rejected to interview
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





# sql database and API's

# API

# an endpoint /blablaa one API that returns all data from SQL data base
# write up structure of return data (fake information)

# main selling point mock Microsoft is GPT cannot do (google Gemini cannot do)
# mock Microsoft

# demonstrate functionality
# time saved (time saved)

# during demo send an email on live
# from a company

# calendar/progress

# send henry emails (maybe)

# flow chart