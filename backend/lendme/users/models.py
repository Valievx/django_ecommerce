from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """ Кастомная модель юзера """
    email = models.EmailField(verbose_name='email address', max_length=200,  unique=True)
    phone_number = models.CharField(verbose_name='phone', max_length=12, unique=True)
    is_phone_verified = models.BooleanField(default=False)
    name = models.CharField(verbose_name='name', max_length=30, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='active', default=True)
    is_staff = models.BooleanField(verbose_name='staff', default=False)
    avatar = models.ImageField(upload_to='users_image', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Review(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_as_seller')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_as_author')
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Отзыв от {self.author} о {self.seller}'

