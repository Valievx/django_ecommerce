from django.shortcuts import render
from django.http import JsonResponse

from catalog.models import Category, Item


def index(request):
    context: dict = {
        'title': 'LendMe - Главная страница',
        'categories': Category.objects.all()
    }

    return render(
        request,
        template_name='main/index.html',
        context=context
    )


def get_items(request):
    offset = int(request.GET.get('offset', 0))
    items = Item.objects.all()[offset: offset+30]
    data = [{
        'name': item.name,
        'image': item.image.url,
        'price': item.price,
        'time_period': item.time_period,
        'time_period_unit': item.time_period_unit,
        'slug': item.slug,
        'pub_date': item.pub_date

    } for item in items]
    return JsonResponse(data, safe=False)
