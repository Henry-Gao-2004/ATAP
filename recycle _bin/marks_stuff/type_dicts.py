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

# Tags

INTERNSHIP = 'internship'
MASTERS = 'masters'
SCHOLARSHIP = 'scholarship'
CLUB = 'club'

COMPLETE = 'complete'
INCOMPLETE = 'incomplete'

SUCCESS = 'success' # green
REJECT = 'reject' # red / maroon
IN_PROGRESS = 'in_progress' # orange

NO_UPDATE = 'no_update' # white

# Email Category Classifier

# just sample method (fix later!)
def app_category_classifier(email: str) -> str | None:
    is_app, _ = is_application(email)
    if not is_app:
        return None

    text = email.lower()

    # simple keyword heuristics
    if 'internship' in text or ' intern ' in text:
        return INTERNSHIP
    if 'master' in text or 'm.s.' in text or 'msc ' in text:
        return MASTERS
    if 'scholarship' in text or 'fellowship' in text:
        return SCHOLARSHIP
    if 'club' in text:
        return CLUB

    # fallback if none match
    return INTERNSHIP

# Internships (run if email is detected to be an internship)

internship_applications = dict()

def internship_insert(email: str) -> None:

    is_app, content = is_application(email) # will probably get rid of this in work flow

    if not is_app:
        return

    success, info = extract_info(email) # make sure this is how extract_info works
    if success and len(info) >= 2:
        company, position = info[0].strip(), info[1].strip()
    else:
        company, position = "Unknown", "Unknown" # just a fallback

    key = f"{company}_{position}"

    entry = {
        "application": {
            "confirmation": COMPLETE,
            "result": IN_PROGRESS
        },
        "assessment": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE
        },
        "interview": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE
        },
        "offer": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE
        },
    }

    internship_applications[key] = entry

# Master's Programs

masters_applications = dict()

def masters_insert(email: str) -> None:

    is_app, content = is_application(email)

    if not is_app:
        return

    success, info = extract_info(email) # make sure this is how extract_info works
    if success and len(info) >= 2:
        school, program = info[0].strip(), info[1].strip()
    else:
        school, program = "Unknown", "Unknown" # just a fallback

    key = f"{school}_{program}"

    entry = {
        "application": {
            "confirmation": COMPLETE,
            "result": IN_PROGRESS
        },
        "assessment": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE
        },
        "interview": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE
        },
        "decision": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE
        },
    }

    masters_applications[key] = entry

# Scholarships (keep in mind that definition of assessment varies with application type)

scholar_applications = dict()

def scholar_insert(email: str) -> None:

    is_app, content = is_application(email)

    if not is_app:
        return

    success, info = extract_info(email) # make sure this is how extract_info works
    if success and len(info) >= 2:
        sponsor, program = info[0].strip(), info[1].strip()
    else:
        sponsor, program = "Unknown", "Unknown" # just a fallback

    key = f"{sponsor}_{program}"

    entry = {
        "application/materials": {
            "confirmation": COMPLETE,
            "result": IN_PROGRESS
        },
        "assessment": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE
        },
        "interview": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE
        },
        "decision": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE
        },
    }

    scholar_applications[key] = entry

# clubs would be weird (not usually a confirmation, but more like a rejection, would have to adjust workflow for clubs)
# Clubs (keep in mind that definition of assessment varies with application type)

club_applications = dict()

def club_insert(email: str) -> None:

    is_app, content = is_application(email)

    if not is_app:
        return

    success, info = extract_info(email) # make sure this is how extract_info works
    if success and len(info) >= 2:
        club = info[0].strip()
    else:
        club = "Unknown" # just a fallback

    key = f"{club}"

    entry = {
        "application/materials": {
            "confirmation": COMPLETE,
            "result": IN_PROGRESS # will get updated when get either accepted/rejected to interview
        },
        "interview": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE
        },
        "decision": {
            "confirmation": INCOMPLETE,
            "result": NO_UPDATE
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