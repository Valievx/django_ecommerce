from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from catalog.models import Category, Item
from catalog.utils import q_search


def catalog(request, category_slug=None):
    category = Category.objects.get(slug=category_slug)
    items = Item.objects.filter(category=category)
    context: dict = {
        'category': category,
        'items': items,
    }

    return render(
        request,
        template_name='catalog/catalog.html',
        context=context
    )


@login_required
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


def search_items(request):
    query = request.GET.get('q', None)
    if query:
        items = q_search(query)
    else:
        items = Item.objects.all()

    context: dict = {
        'items': items,
        'query': query
    }
    return render(
        request,
        'catalog/search_results.html',
        context=context
    )
