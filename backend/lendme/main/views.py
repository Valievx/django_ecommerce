from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: dict[str, str] = {
        'title': 'LendMe - Главная страница'
    }

    return render(
        request,
        template_name='main/index.html',
        context=context
    )
