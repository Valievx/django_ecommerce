from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                       PasswordResetForm, SetPasswordForm,
                                       UserChangeForm)

from users.models import User, Review


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields: list[str] = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'email',
            'phone_number',
            'name',
            'password1',
            'password2',
        )

    email = forms.CharField()
    phone_number = forms.CharField()
    name = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class ProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'avatar',
            'name',
            'email',
            'phone_number'
        )

    avatar = forms.ImageField(required=False)
    name = forms.CharField()
    email = forms.CharField()
    phone_number = forms.CharField()


class UserForgotPasswordForm(PasswordResetForm):
    """ Запрос на восстановление пароля """

    def __init__(self, *args, **kwargs):
        """ Обновление стилей формы """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class UserSetNewPasswordForm(SetPasswordForm):
    """ Изменение пароля пользователя после подтверждения """

    def __init__(self, *args, **kwargs):
        """ Обновление стилей формы """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = (
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    )

    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect(), label='Рейтинг')

    class Meta:
        model = Review
        fields = ('rating', 'comment',)
