from .models import ClientOpinion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache


def get_client_opinions(limit=10):
    """
    Fetches client opinions with an optional limit.

    Args:
        limit (int): The maximum number of client opinions to retrieve. Defaults to 10.

    Returns:
        QuerySet: A queryset of ClientOpinion objects.
    """
    cached_opinions = cache.get('client_opinions')
    if cached_opinions is None:
        try:
            client_opinions = ClientOpinion.objects.all()[:limit]
            cache.set('client_opinions', client_opinions, 300)  # Cache for 5 minutes
            return client_opinions
        except:
            return ClientOpinion.objects.none()
    return cached_opinions


def get_paginated_queryset(queryset, page_number, per_page=2):
    """
    Paginates a queryset for the given page number.

    Args:
        queryset (QuerySet): The queryset to paginate.
        page_number (int or str): The current page number.
        per_page (int): Number of items per page. Defaults to 10.

    Returns:
        Page: A Page object containing the paginated results.
    """
    paginator = Paginator(queryset, per_page)
    try:
        return paginator.page(page_number)
    except (EmptyPage, PageNotAnInteger, ValueError):
        return paginator.page(1)
