from main.models import ContactMessage
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'class': 'form-control shadow-none', 'rows': 4, 'placeholder': 'Type details about your inquiry'}),
        }
