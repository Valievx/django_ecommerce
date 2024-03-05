from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from catalog.models import Category, Item, ItemImage
from catalog.forms import ItemForm, ItemImageForm


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

    if offset > Item.objects.count():
        return JsonResponse({
            'message': 'empty'
        })

    items = Item.objects.all()[offset: offset + 30]
    data = []

    for item in items:
        photos = ItemImage.objects.filter(item=item.id)
        if photos.exists():
            data.append({
                'name': item.name,
                'price': item.price,
                'time_period': item.time_period,
                'slug': item.slug,
                'pub_date': item.pub_date,
                'image': photos.first().image.url
            })

    return JsonResponse(data, safe=False)


@login_required
def additem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        image_form = ItemImageForm(request.POST, request.FILES)
        if form.is_valid() and image_form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.save()

            for file in request.FILES.getlist('image'):
                ItemImage.objects.create(item=item, image=file)

            return redirect('main:index')
    else:
        form = ItemForm()
        image_form = ItemImageForm()

    context = {
        'form': form,
        'image_form': image_form,
        'categories': Category.objects.all()
    }
    return render(
        request,
        template_name='main/additem.html',
        context=context
    )


@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id, author=request.user)
    item_images = ItemImage.objects.filter(item=item)
    previous_image_urls = [image.image.url for image in item_images]

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        image_form = ItemImageForm(request.POST, request.FILES)

        # Удаление изображений
        delete_image_ids = request.POST.getlist('delete_images')
        ItemImage.objects.filter(id__in=delete_image_ids).delete()

        if form.is_valid():
            form.save()

        if image_form.is_valid():
            new_images = request.FILES.getlist('image')
            for image in new_images:
                ItemImage.objects.create(item=item, image=image)
        else:
            if not item_images.exists():
                image_form.add_error(None, "Необходимо загрузить изображение.")

        if form.is_valid() and image_form.is_valid():
            return redirect('catalog:product', product_slug=item.slug)

    else:
        form = ItemForm(instance=item)
        image_form = ItemImageForm(instance=item)

    context = {
        'form': form,
        'image_form': image_form,
        'item': item,
        'item_images': item_images,
        'previous_image_urls': previous_image_urls,
        'categories': Category.objects.all()
    }
    return render(
        request,
        template_name='main/edit_item.html',
        context=context
    )


@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id, author=request.user)

    if request.method == 'POST':
        item.delete()
        return redirect('user:profile', id=request.user.id)

    context = {
        'item': item
    }
    return render(
        request,
        template_name='main/delete_item.html',
        context=context
    )
