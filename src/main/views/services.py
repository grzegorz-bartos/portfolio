from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django_ratelimit.decorators import ratelimit

from ..models import Service
from ..utils import get_client_opinions


@method_decorator(ratelimit(key="ip", rate="10/m", block=True), name="dispatch")
class ServicesView(TemplateView):
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["client_opinions"] = get_client_opinions()
        context["services"] = Service.objects.all()[:8]
        return context
