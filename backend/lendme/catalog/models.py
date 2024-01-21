from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    """ Модель Категорий """
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='URL',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Item(models.Model):
    """ Модель Товара """
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Автор'
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_DEFAULT,
        default='Uncategory',
        related_name='items',
        verbose_name='Категория'
    )
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='URL',
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='items_images',
        verbose_name='Изображение'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('-pub_date',)
