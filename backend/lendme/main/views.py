from django.shortcuts import render, redirect
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
    items = Item.objects.all()[offset: offset + 30]
    data = []

    for item in items:
        photos = ItemImage.objects.filter(item=item)
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
    imageform = ItemImageForm()

    if request.method == 'POST':

        files = request.FILES.getlist('image')

        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.save()

            for file in files:
                ItemImage.objects.create(item=item, image=file)
            return redirect('main:index')
    else:
        form = ItemForm()

    context = {
        'form': form,
        'imageform': imageform,
        'categories': Category.objects.all()
    }
    return render(
        request,
        template_name='main/additem.html',
        context=context
    )
