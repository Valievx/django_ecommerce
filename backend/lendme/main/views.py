from django.shortcuts import render

from catalog.models import Category, Item


def index(request):
    categories = Category.objects.all()
    items = Item.objects.all()

    context: dict = {
        'title': 'LendMe - Главная страница',
        'items': items,
        'categories': categories
    }

    return render(
        request,
        template_name='main/index.html',
        context=context
    )
