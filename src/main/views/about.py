from django_ratelimit.decorators import ratelimit
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

from ..utils import get_client_opinions

@method_decorator(ratelimit(key='ip', rate='10/m', block=True), name='dispatch')
class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = None
        context['client_opinions'] = get_client_opinions()
        return context
