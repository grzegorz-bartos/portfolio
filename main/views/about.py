from django.shortcuts import render
from django_ratelimit.decorators import ratelimit

from main.utils import get_client_opinions


@ratelimit(key='ip', rate='10/m', block=True)
def about(request):
    brands = None
    client_opinions = get_client_opinions()

    context = {
        'brands': brands,
        'client_opinions': client_opinions
    }
    return render(request, 'about.html', context)