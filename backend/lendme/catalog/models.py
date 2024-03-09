from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime
from unidecode import unidecode

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
        blank=True,
        null=True,
        verbose_name='URL',
    )
    image = models.ImageField(
        upload_to='categories',
        verbose_name='Изображение'
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
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Категория'
    )
    name = models.CharField(
        max_length=200,
        unique=False,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='URL',
        blank=True,
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.IntegerField(
        verbose_name='Цена'
    )
    time_period = models.CharField(
        max_length=20,
        choices=[
            ('Час', 'Час'),
            ('Сутки', 'Сутки'),
            ('Месяц', 'Месяц'),
        ],
        verbose_name='Период времени'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    def save(self, *args, **kwargs):
        if self.name.isascii():
            self.slug = self.name.lower()
        else:
            self.slug = unidecode(self.name).lower()

        self.slug = self.slug.replace("'", "y")  # Заменяем 'ь, ъ' на 'y'
        self.slug = self.slug.replace(' ', '_')
        self.slug = self.slug + "_{:%Y%m%d%H%M%S}".format(datetime.now())

        super(Item, self).save(*args, **kwargs)

    @property
    def price_with_symbol(self):
        return f'{self.price} ₽/{self.time_period}'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('-pub_date',)


class ItemImage(models.Model):
    """ Модель изображения товара """
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name='Товар'
    )
    image = models.ImageField(
        upload_to='items',
        verbose_name='Изображение'
    )

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Favorite(models.Model):
    """ Модель Избранного"""
    item = models.ForeignKey(
        Item,
        related_name='favorite',
        verbose_name='Товар',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        related_name='favorite',
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

        constraints = (
            models.UniqueConstraint(
                fields=(
                    'item',
                    'user',
                ),
                name='unique_favorite',
            ),
        )

    def __str__(self):
        return f'{self.item.name}'
