# context_processors.py
from .models import Profile

def personal_information(request):
    profile = Profile.objects.first()
    if profile is None:
        context = {
            "YEARS_OF_EXPERIENCE": 0,
            "AVAILABILITY": False,
            "GITHUB": "",
            "LINKEDIN": "",
            "DISCORD": "",
            "CLIENT_COUNT": 0,
            "PROJECTS_COMPLETED": 0,
        }
    else:
        context = {
            "YEARS_OF_EXPERIENCE": profile.years_of_experience,
            "AVAILABILITY": profile.availability,
            "GITHUB": profile.github,
            "LINKEDIN": profile.linkedin,
            "DISCORD": profile.discord,
            "CLIENT_COUNT": profile.client_count,
            "PROJECTS_COMPLETED": profile.projects_completed,
        }
    return context
