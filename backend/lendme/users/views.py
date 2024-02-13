from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from catalog.models import Item
from users.forms import (UserLoginForm, UserRegistrationForm,
                         ProfileForm)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context: dict = {
        'title': 'Lendme - Авторизация',
        'form': form
    }
    return render(
        request,
        template_name='users/login.html',
        context=context
    )


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))

    else:
        form = UserRegistrationForm()

    context: dict = {
        'title': 'Lendme - Регистрация',
        'form': form,
    }
    return render(
        request,
        template_name='users/login.html',
        context=context
    )


@login_required
def profile(request):
    ads = Item.objects.filter(author=request.user)
    if request.method == 'POST':
        form = ProfileForm(
            data=request.POST,
            instance=request.user,
            files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш профиль успешно обновлен')
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = ProfileForm(instance=request.user)

    context: dict = {
        'title': 'Lendme - Регистрация',
        'form': form,
        'ads': ads
    }
    return render(
        request,
        template_name='users/profile.html',
        context=context
    )


@login_required
def logout(request):
    messages.success(request, f'{request.user.username} Вы вышли из аккаунта')
    auth.logout(request)
    return redirect(reverse('main:index'))
