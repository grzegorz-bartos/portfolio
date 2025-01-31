from django.db import models
from django import forms
from django.urls import reverse_lazy
from django.views.generic import FormView


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')  # Redirects after successful submission

    def form_valid(self, form):
        form.save()  # Saves the form data to the database
        return super().form_valid(form)
