from django.db import models
from django import forms


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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'class': 'form-control shadow-none', 'rows': 4, 'placeholder': 'Type details about your inquiry'}),
        }
