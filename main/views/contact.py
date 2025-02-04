from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django_ratelimit.decorators import ratelimit
from main.models.contact_message import ContactForm


@method_decorator(ratelimit(key='ip', rate='10/m', block=True), name='dispatch')
class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')

