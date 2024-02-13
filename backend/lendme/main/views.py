from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from catalog.models import Category, Item
from catalog.forms import ItemForm


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
        'slug': item.slug,
        'pub_date': item.pub_date

    } for item in items]
    return JsonResponse(data, safe=False)


@login_required
def additem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST or None,
                        files=request.FILES or None
                        )
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.save()
            return redirect('main:index')
    else:
        form = ItemForm()

    context = {
        'form': form,
        'categories': Category.objects.all()
    }
    return render(
        request,
        template_name='main/additem.html',
        context=context
    )
