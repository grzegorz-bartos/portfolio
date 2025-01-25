from django.shortcuts import get_object_or_404, render
from django_ratelimit.decorators import ratelimit

from main.models import Article


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