from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django_ratelimit.decorators import ratelimit

from main.models import Project
from main.utils import get_paginated_queryset



@method_decorator(ratelimit(key='ip', rate='10/m', block=True), name='dispatch')
class PortfolioView(ListView):
    model = Project
    template_name = 'portfolio.html'
    context_object_name = 'page_obj'
    paginate_by = 10

    def get_queryset(self):
        return Project.objects.all()
