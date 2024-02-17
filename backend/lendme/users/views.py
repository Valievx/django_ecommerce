from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin

from users.models import User
from catalog.models import Item, ItemImage
from .forms import (UserLoginForm, UserRegistrationForm,
                    ProfileForm, UserForgotPasswordForm,
                    UserSetNewPasswordForm)


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
        template_name='users/registration.html',
        context=context
    )


@login_required
def profile_edit(request):
    items = Item.objects.filter(author=request.user)
    photos_preview = []

    for item in items:
        image = ItemImage.objects.filter(item=item).first()
        if image:
            photos_preview.append(image)

    if request.method == 'POST':
        form = ProfileForm(
            data=request.POST,
            instance=request.user,
            files=request.FILES
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = ProfileForm(instance=request.user)

    context: dict = {
        'title': 'Lendme - Регистрация',
        'form': form,
        'items': items,
        'photos_preview': photos_preview
    }
    return render(
        request,
        template_name='users/profile_edit.html',
        context=context
    )


@login_required
def profile(request, id):
    author = get_object_or_404(User, id=id)
    items = Item.objects.filter(author=author)

    context = {
        'author': author,
        'items': items,
    }
    return render(
        request,
        template_name='users/profile.html',
        context=context
    )


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))


class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    """ Представление по сбросу пароля по почте """
    form_class = UserForgotPasswordForm
    template_name = 'users/user_password_reset.html'
    success_url = '/user/password-reset/'
    success_message = 'Письмо с инструкцией по восстановлению пароля отправлено на ваш email'
    subject_template_name = 'users/email/password_subject_reset_mail.txt'
    email_template_name = 'users/email/password_reset_mail.html'

    def get_success_message(self, cleaned_data):
        return self.success_message

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запрос на восстановление пароля'
        return context


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    """ Представление установки нового пароля """
    form_class = UserSetNewPasswordForm
    template_name = 'users/user_password_set_new.html'
    success_url = '/user/set-new-password/MQ/set-password/'
    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'

    def get_success_message(self, cleaned_data):
        return self.success_message

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Установить новый пароль'
        return context
