from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django_ratelimit.decorators import ratelimit

from main.models import Article


@method_decorator(ratelimit(key='ip', rate='10/m', block=True), name='dispatch')
class BlogView(ListView):
    model = Article
    template_name = 'blog.html'
    paginate_by = 4
