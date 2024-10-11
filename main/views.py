from django.shortcuts import render
from .models import (ExpertArea, Project, Service, WorkExperience, Article)
from .utils import get_client_opinions
from django.core.paginator import Paginator


def home(request):
    expert_areas = ExpertArea.objects.all()
    work_experiences = WorkExperience.objects.all()[:10]
    projects = Project.objects.all()[:2]
    services_list = Service.objects.all()[:4]
    context = {
        'expert_areas': expert_areas,
        'work_experiences': work_experiences,
        'projects': projects,
        'services_list': services_list,
    }
    return render(request, 'base.html', context)


def about(request):
    brands = None
    client_opinions = get_client_opinions()

    context = {
        'brands': brands,
        'client_opinions': client_opinions}
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


def portfolio_details(request):
    return render(request, 'portfolio-details.html')


def blog(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, 'blog.html', context)


def article(request):
    return render(request, 'article.html')


def contact(request):
    return render(request, 'contact.html')
