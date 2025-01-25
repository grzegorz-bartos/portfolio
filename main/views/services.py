from django.shortcuts import render
from django_ratelimit.decorators import ratelimit

from main.models import Service
from main.utils import get_client_opinions


@ratelimit(key='ip', rate='10/m', block=True)
def services(request):
    client_opinions = get_client_opinions()
    services_list = Service.objects.all()[:8]
    context = {
        'client_opinions': client_opinions,
        'services': services_list,
    }
    return render(request, 'services.html', context)