from nlp_utils import is_application

def test_is_application():
    email = """You are receiving this email because you joined the Ansys Talent Community on 6/23/23. You will receive these messages every 7 day(s). Your Job Alert matched the following jobs at careers.ansys.com.

Jobs
R&D Engineer II - Austin, TX, US, 78746
Fall 2025 Co-Op - Software Development - Mechanical (Bachelors/Masters/PhD) - Canonsburg, PA, US, 15317
Fall 2025 Intern - Technical Writing - Mechanical (Bachelors/Masters) - Canonsburg, PA, US, 15317
Fall 2025 Intern - Meshing (Bachelors/Masters) - Canonsburg, PA, US, 15317
R&D Verification Engineer II - Canonsburg, PA, US, 15317
Senior Enterprise Account Executive - Military/Federal - REMOTE - Exton, PA, US, 19341
Product Sales Executive - Autonomous Vehicle - REMOTE - Novi, MI, US, 48375
Senior Enterprise Account Executive - Austin, TX, US, 78746
Senior Customer Project Manager - Pipeline and Portfolio Management (Remote) - Canonsburg, PA, US, 15317
R&D Engineer II - Canonsburg, PA, US, 15317



Manage your Job Alerts"""
    result = is_application(email)
    assert result[1] == "True", f"Expected True but got {result}"

if __name__ == "__main__":
    test_is_application()
    print("Test passed!")
