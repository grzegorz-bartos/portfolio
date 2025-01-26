from django.shortcuts import render
from django_ratelimit.decorators import ratelimit
from main.models import Article
from main.utils import get_paginated_queryset

@ratelimit(key='ip', rate='10/m', block=True)
def blog(request):
    articles = Article.objects.all()

    page_number = request.GET.get('page', 1)

    page_obj = get_paginated_queryset(articles, page_number, per_page=4)

    context = {
        "page_obj": page_obj,
    }
    return render(request, 'blog.html', context)