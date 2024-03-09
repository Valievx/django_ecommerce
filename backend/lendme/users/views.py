from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404

from catalog.models import Item, ItemImage, Favorite
from .models import User, Review
from .forms import (UserLoginForm, UserRegistrationForm,
                    ProfileForm, UserForgotPasswordForm,
                    UserSetNewPasswordForm, ReviewForm)


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
    reviews = Review.objects.filter(seller=author)

    # Подсчет среднего рейтинга
    total_rating = 0
    for review in reviews:
        total_rating += review.rating

    if reviews.count() > 0:
        average_rating = total_rating / reviews.count()
        average_rating = round(average_rating, 1)
    else:
        average_rating = 0

    seller_id = author.id

    # Получаем все товары, добавленные в избранное пользователем
    favorite_items = Favorite.objects.filter(user=request.user)

    # Создаем множество из id товаров, добавленных в избранное пользователем
    favorite_item_id = set(favorite_item.item.id for favorite_item in favorite_items)

    context = {
        'author': author,
        'items': items,
        'seller_id': seller_id,
        'reviews': reviews,
        'average_rating': average_rating,
        'favorite_item_id': favorite_item_id,
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


@login_required
def create_review(request, seller_id):
    """ Представление создания отзыва"""
    seller = get_object_or_404(User, id=seller_id)
    reviews = Review.objects.filter(seller=seller).order_by('-created_at')

    if request.user == seller:
        return HttpResponse("Вы не можете оставить отзыв самому себе.")

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.seller = seller
            review.author = request.user
            review.save()
            form = ReviewForm()
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'seller_id': seller_id,
        'reviews': reviews
    }

    return render(
        request,
        template_name='users/review.html',
        context=context
    )


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user == review.author:
        review.delete()
    else:
        raise Http404("У вас нет разрешения на удаление этого отзыва.")
    return create_review(request, review.seller.id)


@login_required
def my_reviews(request, user_id):
    user = get_object_or_404(User, id=user_id)
    reviews = Review.objects.filter(seller=user).order_by('-created_at')

    context = {
        'user': user,
        'reviews': reviews,
    }
    return render(request, 'users/my_reviews.html', context=context)


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

