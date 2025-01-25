from django.shortcuts import render

def rate_limit_exceeded(request):
    """
    Custom view to handle rate-limited requests.
    """
    # For HTML response
    return render(request, 'rate_limit.html', status=429)

    # Uncomment the following line for a JSON response
    # return JsonResponse({'error': 'Too many requests. Please try again later.'}, status=429)