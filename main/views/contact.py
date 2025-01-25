from django.shortcuts import render
from django_ratelimit.decorators import ratelimit


@ratelimit(key='ip', rate='10/m', block=True)
def contact(request):
    return render(request, 'contact.html')