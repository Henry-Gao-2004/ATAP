from nlp_utils import *
from database.sql_database import *
from database.flow import *
import uuid

# Constants

## Application Types
INTERNSHIP = 'internship'
POST_GRAD = 'post_grad'
SCHOLARSHIP = 'scholarship'
CLUB = 'club'

## Confirmation
COMPLETE = 'complete'
INCOMPLETE = 'incomplete'

## Result
SUCCESS = 'success'
REJECT = 'reject'
IN_PROGRESS = 'in_progress'
NO_UPDATE = 'no_update'

## Stage
APPLICATION = 'application'
ASSESSMENT = 'assessment'
INTERVIEW = 'interview'
OFFER = 'offer'
DECISION = 'decision'

# Defining method to obtain last completed stage (for rejection purposes)
## Stage-aware rejection check
def get_latest_stage(app_type: str, key: str) -> str:
    app_dict = {
        INTERNSHIP: internship_applications,
        POST_GRAD: masters_applications,
        SCHOLARSHIP: scholar_applications,
        CLUB: club_applications
    }

    stage_order_map = {
        INTERNSHIP: [APPLICATION, ASSESSMENT, INTERVIEW],
        POST_GRAD: [APPLICATION, ASSESSMENT, INTERVIEW],
        SCHOLARSHIP: [APPLICATION, INTERVIEW],
        CLUB: [APPLICATION, INTERVIEW]
    }

    record = app_dict.get(app_type, {}).get(key)
    if not record:
        return APPLICATION  # Fallback if no entry found

    for stage in reversed(stage_order_map.get(app_type, [])):
        if record.get(stage, {}).get("result") == IN_PROGRESS:
            return stage

    return APPLICATION # Fallback if nothing is complete

# Flow Dispatch Map (without rejections)
## No need to be stage-aware because email content will be enough to tell what stage application is at
flow_dispatch = {
    (INTERNSHIP, "assessment_invite"): assessment_invite_update_int,
    (INTERNSHIP, "assessment_confirmation"): assessment_confirmation_int,
    (INTERNSHIP, "interview_invite"): interview_invite_update_int,
    (INTERNSHIP, "interview_confirmation"): interview_confirmation_int,
    (INTERNSHIP, "decision_update"): offer_update_int,

    (POST_GRAD, "assessment_invite"): assessment_invite_update_post,
    (POST_GRAD, "assessment_confirmation"): assessment_confirmation_post,
    (POST_GRAD, "interview_invite"): interview_invite_update_post,
    (POST_GRAD, "interview_confirmation"): interview_confirmation_post,
    (POST_GRAD, "decision_update"): decision_update_post,

    (SCHOLARSHIP, "interview_invite"): interview_invite_update_schol,
    (SCHOLARSHIP, "interview_confirmation"): interview_confirmation_schol,
    (SCHOLARSHIP, "decision_update"): decision_update_schol,

    (CLUB, "interview_invite"): interview_invite_update_club,
    (CLUB, "interview_confirmation"): interview_confirmation_club,
    (CLUB, "offer_update"): offer_update_club
}

# Rejection Dispatch Map (stage-aware)
## Need rejections to be stage-aware because usually just plain rejection
rejection_dispatch = {
    (APPLICATION, INTERNSHIP): rejection_update_application_int,
    (ASSESSMENT, INTERNSHIP): rejection_update_assessment_int,
    (INTERVIEW, INTERNSHIP): rejection_update_interview_int,

    (APPLICATION, POST_GRAD): rejection_update_application_post,
    (ASSESSMENT, POST_GRAD): rejection_update_assessment_post,
    (INTERVIEW, POST_GRAD): rejection_update_interview_post,

    (APPLICATION, SCHOLARSHIP): rejection_update_application_schol,
    (INTERVIEW, SCHOLARSHIP): rejection_update_interview_schol,

    (APPLICATION, CLUB): rejection_update_application_club,
    (INTERVIEW, CLUB): rejection_update_interview_club,
}

# Constructing final workflow
def final_workflow(email: str) -> None:
    task_uuid = uuid.uuid4()
    print(datetime.now().strftime("%H:%M:%S"),task_uuid,"Starting ...")

    # 1. Check if email is application-related
    print(datetime.now().strftime("%H:%M:%S"),task_uuid,"Checking if email is application-related...")
    is_app, content = is_application(email)
    print(datetime.now().strftime("%H:%M:%S"),task_uuid,"Is application-related:", is_app)
    if not is_app:
        return

    #2. Classify email type
    print(datetime.now().strftime("%H:%M:%S"),task_uuid,"Classifying email category...")
    success, category = classify_category(email)
    print(datetime.now().strftime("%H:%M:%S"),task_uuid,"Classified category:", category)
    if success:
        category = category.lower() # make sure using this right
        category_map = {
            "internship": INTERNSHIP,
            "club": CLUB,
            "education": POST_GRAD,
            "scholarship": SCHOLARSHIP
        }

        app_type = category_map.get(category)
        if not app_type:
            print(datetime.now().strftime("%H:%M:%S"),task_uuid,"Unrecognized category:", category)
            return # Fallback in case of unrecognized category
    else:
        return # Fallback in case of failure to classify

    #3. Creating Keys and Entries (if unique key)

    print(datetime.now().strftime("%H:%M:%S"),task_uuid,"Extracting information from email...")
    success, info = extract_info(email)
    print(datetime.now().strftime("%H:%M:%S"),task_uuid,"Extracted info:", info)

    if app_type == INTERNSHIP and success and len(info) >= 2:
        company = info[0].strip().replace(" ", "_")
        position = info[1].strip().replace(" ", "_")
        key = f"{company}_{position}"
        if key not in internship_applications:
            internship_insert(key)

    elif app_type == POST_GRAD and success and len(info) >= 2:
        school = info[0].strip().replace(" ", "_")
        program = info[1].strip().replace(" ", "_")
        key = f"{school}_{program}"
        if key not in masters_applications:
            masters_insert(key)

    elif app_type == SCHOLARSHIP and success and len(info) >= 1:
        scholarship = info[0].strip().replace(" ", "_")
        key = scholarship
        if key not in scholar_applications:
            scholar_insert(key)

    elif app_type == CLUB and success and len(info) >= 1:
        club = info[0].strip().replace(" ", "_")
        key = club
        if key not in club_applications:
            club_insert(key)

    #4. Determine action type from email
    print(datetime.now().strftime("%H:%M:%S"),task_uuid,"Determining action type from email...")
    action_type = email_action(email)[1]
    print(datetime.now().strftime("%H:%M:%S"),task_uuid,"Action type:", action_type)

    #5. Rejection handling
    if action_type == "rejection":
        latest_stage = get_latest_stage(app_type, key)
        rejection_func = rejection_dispatch.get((latest_stage, app_type))
        rejection_func(key)

    #6. Handle all other actions
    else:
        update_func = flow_dispatch.get((app_type, action_type))
        update_func(key)

    #7 Persist update to SQLite
    if app_type == INTERNSHIP:
        persist_internships({key: internship_applications[key]})
    elif app_type == POST_GRAD:
        persist_masters({key: masters_applications[key]})
    elif app_type == SCHOLARSHIP:
        persist_scholarships({key: scholar_applications[key]})
    elif app_type == CLUB:
        persist_clubs({key: club_applications[key]})

# everything is flexible besides for getting initial email (non-negotiable)

# in the future change from grouped updates to precise updates
# for redundancy avoidance, do a method (rn very explicit)

# delete after 12 months (or somehow make applications unique - change key names?)

# calendar
# progress

# database for each user, user_id (when multiple users)

# add fallback checks later

# separate into more concrete .py files

