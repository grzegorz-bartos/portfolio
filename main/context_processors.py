from datetime import date


def personal_information(request):
    context = {
        "YEARS_OF_EXPERIENCE": date.today().year - 2021,
        "AVAILABILITY": True,
        "GITHUB": "https://github.com/Grzegorz-Bartos",
        "LINKEDIN": "https://www.linkedin.com/in/grzegorz-bartos/",
        "DISCORD": "https://discord.gg/Wj6hjPvPXC",
        "CLIENT_COUNT": 30,
        "PROJECTS_COMPLETED": 10,
    }
    return context

