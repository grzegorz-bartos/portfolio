from django.shortcuts import render
from django_ratelimit.decorators import ratelimit

from main.models import ExpertArea, Certificate, Project, Service


@ratelimit(key='ip', rate='10/m', block=False)
def home(request):
    was_limited = getattr(request, 'limited', False)
    if was_limited:
        return render(request, 'rate_limit.html')

    expert_areas = ExpertArea.objects.all()[:6]
    certificates = Certificate.objects.all()[:10]
    certificates = list(certificates)
    if len(certificates) > 4:
        certificates *= 2  # duplicate items for better scrolling animation
    projects = Project.objects.all()[:2]
    services_list = Service.objects.all()[:4]
    context = {
        'expert_areas': expert_areas,
        'certificates': certificates,
        'projects': projects,
        'services': services_list,
    }
    return render(request, 'home.html', context) # home.html