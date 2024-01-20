from django.shortcuts import render


def catalog(request):
    return render(
        request,
        template_name='catalog/catalog.html',
    )


def product(request):
    return render(
        request,
        template_name='catalog/product.html',
    )
