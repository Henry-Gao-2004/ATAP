# Constants
INTERNSHIP = 'internship'
POST_GRAD = 'post_grad'
SCHOLARSHIP = 'scholarship'
CLUB = 'club'

COMPLETE = 'complete'
INCOMPLETE = 'incomplete'

SUCCESS = 'success'
REJECT = 'reject'
IN_PROGRESS = 'in_progress'
NO_UPDATE = 'no_update'

APPLICATION = 'application'
ASSESSMENT = 'assessment'
INTERVIEW = 'interview'
OFFER = 'offer'
DECISION = 'decision'

# Creating global dictionaries (make sure works with methods from type_dicts)
internship_applications = dict()
masters_applications = dict()  # fix to post_grad later
scholar_applications = dict()
club_applications = dict()

# Defining method to obtain last completed stage (for rejection purposes)
# Stage-aware rejection check
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
# No need to be stage-aware because email content will be enough to tell what stage application is at
flow_dispatch = {
    (INTERNSHIP, "assessment_invite"): assessment_invite_update_int,
    (INTERNSHIP, "assessment_confirmation"): assessment_confirmation_int,
    (INTERNSHIP, "interview_invite"): interview_invite_update_int,
    (INTERNSHIP, "interview_confirmation"): interview_confirmation_int,
    (INTERNSHIP, "offer_update"): offer_update_int,

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
# Need rejections to be stage-aware because usually just plain rejection
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

def final_workflow(email: str) -> None:

    # 1. Check if email is application-related
    is_app, content = is_application(email)
    if not is_app:
        return

    #2. Classify email type
    success, category_list = classify_category(email)
    if success:
        category = category_list[0].lower() # make sure using this right
        category_map = {
            "internship": INTERNSHIP,
            "club": CLUB,
            "education": POST_GRAD,
            "scholarship": SCHOLARSHIP
        }

        app_type = category_map.get(category)
        if not app_type:
            return # Fallback in case of unrecognized category
    else:
        return # Fallback in case of failure to classify

    #3. Creating Keys and Entries (if unique key)

    success, info = extract_info(email)

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
    action_type = email_action(email)

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

# figuring out time thing (figure out flow and how to not update if already updated)
