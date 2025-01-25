from django.shortcuts import get_object_or_404, render
from django_ratelimit.decorators import ratelimit

from main.models import Project


@ratelimit(key='ip', rate='10/m', block=True)
def portfolio_details(request, slug):
    project = get_object_or_404(Project, slug=slug)
    additional_images = project.additional_images.all()[:2]
    services_list = list(project.services.values_list('name', flat=True))

    if len(services_list) > 1:
        services_formatted = ', '.join(services_list[:-1]) + ', and ' + services_list[-1]
    elif services_list:
        services_formatted = services_list[0]
    else:
        services_formatted = None

    previous_project = Project.objects.filter(id__lt=project.id).order_by('-id').first()
    next_project = Project.objects.filter(id__gt=project.id).order_by('-id').first()

    context = {
        'project': project,
        'additional_images': additional_images,
        'services_formatted': services_formatted,
        'previous_project': previous_project,
        'next_project': next_project,
    }
    return render(request, 'portfolio-details.html', context)