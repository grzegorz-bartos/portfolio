from django.shortcuts import render, get_object_or_404
from .models import (ExpertArea, Project, Service, Certificate, Article)
from .utils import get_client_opinions
from django.core.paginator import Paginator


def home(request):
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


def about(request):
    brands = None
    client_opinions = get_client_opinions()

    context = {
        'brands': brands,
        'client_opinions': client_opinions
    }
    return render(request, 'about.html', context)


def services(request):
    client_opinions = get_client_opinions()
    services_list = Service.objects.all()[:8]
    context = {
        'client_opinions': client_opinions,
        'services': services_list,
    }
    return render(request, 'services.html', context)


def portfolio(request):
    projects = Project.objects.all()
    paginator = Paginator(projects, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,  # Ensure you pass it as 'page_obj'
    }
    return render(request, 'portfolio.html', context)


def portfolio_details(request, project_id):
    project = get_object_or_404(Project, id=project_id)
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


def blog(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, 'blog.html', context)


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


def contact(request):
    return render(request, 'contact.html')
