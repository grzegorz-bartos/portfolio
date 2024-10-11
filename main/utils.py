from .models import ClientOpinion


def get_client_opinions():
    client_opinions = ClientOpinion.objects.all()[:10]
    for opinion in client_opinions:
        opinion.stars_range = range(opinion.stars)
    return client_opinions
