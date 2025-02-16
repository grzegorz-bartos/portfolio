from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django_ratelimit.decorators import ratelimit

from ..models import Article


@method_decorator(ratelimit(key="ip", rate="10/m", block=True), name="dispatch")
class BlogArticleView(DetailView):
    model = Article
    template_name = "article.html"
    pk_url_kwarg = "article_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.object

        context["previous_article"] = (
            Article.objects.filter(id__lt=article.id).order_by("-id").first()
        )
        context["next_article"] = (
            Article.objects.filter(id__gt=article.id).order_by("id").first()
        )

        return context
