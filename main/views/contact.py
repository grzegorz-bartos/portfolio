from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django_ratelimit.decorators import ratelimit


@method_decorator(ratelimit(key='ip', rate='10/m', block=True), name='dispatch')
class ContactView(TemplateView):
    template_name = 'contact.html'
