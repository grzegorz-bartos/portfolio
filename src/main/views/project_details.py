from django.views.generic import DetailView
from django.shortcuts import get_object_or_404, render
from django_ratelimit.decorators import ratelimit
from main.models import Project
from django.utils.decorators import method_decorator

@method_decorator(ratelimit(key='ip', rate='10/m', block=False), name='dispatch')
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project-details.html'
    context_object_name = 'project'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Project, slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object

        # Additional images
        context['additional_images'] = project.additional_images.all()[:2]

        # Services list formatting
        services_list = list(project.services.values_list('name', flat=True))
        if len(services_list) > 1:
            context['services_formatted'] = ', '.join(services_list[:-1]) + ', and ' + services_list[-1]
        elif services_list:
            context['services_formatted'] = services_list[0]
        else:
            context['services_formatted'] = None

        # Previous and next project
        context['previous_project'] = Project.objects.filter(id__lt=project.id).order_by('-id').first()
        context['next_project'] = Project.objects.filter(id__gt=project.id).order_by('-id').first()

        return context
