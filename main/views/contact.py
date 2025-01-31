from django.utils.decorators import method_decorator
from django.views.generic import View
from django_ratelimit.decorators import ratelimit
from django.shortcuts import render, redirect
from main.models.contact_message import ContactForm


@method_decorator(ratelimit(key='ip', rate='10/m', block=True), name='dispatch')
class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
        return render(request, 'contact.html', {'form': form})
