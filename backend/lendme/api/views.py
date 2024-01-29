from django.http import JsonResponse
from ..catalog.models import Item


def get_posts(request):
    items = Item.objects.all()
    data = []
    for item in items:
        data.append({
            'name': item.name,
            'content': item.description,
        })
    return JsonResponse(data, safe=False)
