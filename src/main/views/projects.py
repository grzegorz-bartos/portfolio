from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django_ratelimit.decorators import ratelimit

from ..models import Project


@method_decorator(ratelimit(key="ip", rate="10/m", block=True), name="dispatch")
class ProjectsView(ListView):
    model = Project
    template_name = "projects.html"
    paginate_by = 1

    def get_queryset(self):
        return Project.objects.all()
