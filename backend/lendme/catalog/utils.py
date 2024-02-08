from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from catalog.models import Item


def q_search(query):
    """ Функция поиска """
    if query.isdigit() and len(query) <= 5:
        return Item.objects.filter(id=int(query))

    vector = SearchVector('name', 'description')
    query = SearchQuery(query)

    return (
        Item.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by('-rank')
    )
