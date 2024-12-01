from django.shortcuts import render, get_object_or_404
from .models import (ExpertArea, Project, Service, Certificate, Article)
from .utils import get_client_opinions, get_paginated_queryset
from django_ratelimit.decorators import ratelimit
from django.http import JsonResponse


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
    return render(request, 'base.html', context)


@ratelimit(key='ip', rate='10/m', block=True)
def about(request):
    brands = None
    client_opinions = get_client_opinions()

    context = {
        'brands': brands,
        'client_opinions': client_opinions
    }
    return render(request, 'about.html', context)


@ratelimit(key='ip', rate='10/m', block=True)
def services(request):
    client_opinions = get_client_opinions()
    services_list = Service.objects.all()[:8]
    context = {
        'client_opinions': client_opinions,
        'services': services_list,
    }
    return render(request, 'services.html', context)


@ratelimit(key='ip', rate='10/m', block=True)
def portfolio(request):
    projects = Project.objects.all()

    page_number = request.GET.get('page', 1)
    page_obj = get_paginated_queryset(projects, page_number)

    context = {
        "page_obj": page_obj,  # Ensure you pass it as 'page_obj'
    }
    return render(request, 'portfolio.html', context)


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


@ratelimit(key='ip', rate='10/m', block=True)
def blog(request):
    articles = Article.objects.all()

    page_number = request.GET.get('page', 1)

    page_obj = get_paginated_queryset(articles, page_number, per_page=4)

    context = {
        "page_obj": page_obj,
    }
    return render(request, 'blog.html', context)


@ratelimit(key='ip', rate='10/m', block=True)
def blog_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    previous_article = Article.objects.filter(id__lt=article.id).order_by('-id').first()
    next_article = Article.objects.filter(id__gt=article.id).order_by('id').first()

    context = {
        'article': article,
        'previous_article': previous_article,
        'next_article': next_article,
    }
    return render(request, 'article.html', context)


@ratelimit(key='ip', rate='10/m', block=True)
def contact(request):
    return render(request, 'contact.html')


def rate_limit_exceeded(request):
    """
    Custom view to handle rate-limited requests.
    """
    # For HTML response
    return render(request, 'rate_limit.html', status=429)

    # Uncomment the following line for a JSON response
    # return JsonResponse({'error': 'Too many requests. Please try again later.'}, status=429)
