from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from catalog.models import Category, Item, ItemImage, Favorite
from catalog.utils import q_search


def catalog(request, category_slug=None):
    category = Category.objects.get(slug=category_slug)
    items = Item.objects.filter(category=category)

    # Получаем список id товаров, добавленных в избранное текущим пользователем
    favorite_items_ids = Favorite.objects.filter(user=request.user).values_list('item__id', flat=True)

    for item in items:
        item.image = ItemImage.objects.filter(item=item).first()
        # Проверяем, добавлен ли товар в избранное текущим пользователем
        item.is_added_to_favorite = item.id in favorite_items_ids

    context = {
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
    photos = ItemImage.objects.filter(item=product)
    photo_preview = photos.first()

    # Проверяем, добавлен ли товар в избранное текущим пользователем
    is_added_to_favorite = False
    if request.user.is_authenticated:
        is_added_to_favorite = Favorite.objects.filter(item=product, user=request.user).exists()

    context = {
        'product': product,
        'photos': photos,
        'photo_preview': photo_preview,
        'is_added_to_favorite': is_added_to_favorite  # Добавляем переменную состояния кнопки лайка
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

    photos_preview = []
    for item in items:
        image = ItemImage.objects.filter(item=item).first()
        if image:
            photos_preview.append(image)

    # Проверяем, добавлен ли каждый элемент в избранное текущим пользователем
    favorite_items_id = Favorite.objects.filter(user=request.user, item__in=items).values_list('item_id', flat=True)

    context: dict = {
        'items': items,
        'photos_preview': photos_preview,
        'query': query,
        'favorite_items_id': favorite_items_id,
    }
    return render(
        request,
        'catalog/search_results.html',
        context=context
    )
