from django.shortcuts import render
from catalog.models import Item


def catalog(request):
    context: dict = {
        'title': 'LendMe - Каталог',
    }

    return render(
        request,
        template_name='catalog/catalog.html',
        context=context
    )


def product(request, product_slug):
    product = Item.objects.get(slug=product_slug)
    context: dict = {
        'product': product,
    }
    return render(
        request,
        template_name='catalog/product.html',
        context=context
    )
