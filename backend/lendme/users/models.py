from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    """ Кастомная модель юзера """
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name'
    ]
    email = models.EmailField(
        max_length=254,
        unique=True
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='first name'
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='last name'
    )
    username = models.CharField(
        max_length=150,
        verbose_name='username',
        validators=[RegexValidator(
            regex=r'^[\w.@+-]+\Z',
            message='Недопустимые символы')
        ]
    )
    image = models.ImageField(
        upload_to='users_image',
        blank=True,
        null=True,
        verbose_name='avatar'
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    @property
    def in_moderator(self):
        return self.is_staff

    @property
    def is_admin(self):
        return self.is_superuser
