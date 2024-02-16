from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                       PasswordResetForm, SetPasswordForm,
                                       UserChangeForm)

from users.models import User


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
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

    email = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class ProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'avatar',
            'first_name',
            'last_name',
            'email',
        )

    avatar = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()


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
