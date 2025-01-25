from django.shortcuts import render
from django_ratelimit.decorators import ratelimit

from main.models import Project
from main.utils import get_paginated_queryset


@ratelimit(key='ip', rate='10/m', block=True)
def portfolio(request):
    projects = Project.objects.all()

    page_number = request.GET.get('page', 1)
    page_obj = get_paginated_queryset(projects, page_number)

    context = {
        "page_obj": page_obj,  # Ensure you pass it as 'page_obj'
    }
    return render(request, 'portfolio.html', context)