from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django_ratelimit.decorators import ratelimit

from ..models import Certificate, ExpertArea, Project, Service


@method_decorator(ratelimit(key="ip", rate="10/m", block=False), name="dispatch")
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        expert_areas = ExpertArea.objects.all()[:6]
        certificates = Certificate.objects.all()[:10]
        if len(certificates) > 4:
            certificates *= 2  # duplicate items for better scrolling animation
        context["expert_areas"] = expert_areas
        context["certificates"] = certificates
        context["projects"] = Project.objects.all()[:2]
        context["services"] = Service.objects.all()[:4]
        return context
