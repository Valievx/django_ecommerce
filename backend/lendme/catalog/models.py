from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

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
        unique=True,
        verbose_name='URL',
        blank=True,
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='items',
        verbose_name='Изображение'
    )
    price = models.IntegerField(
        verbose_name='Цена'
    )
    time_period = models.PositiveIntegerField(
        verbose_name='Период времени'
    )
    time_period_unit = models.CharField(
        max_length=20,
        choices=[
            ('День', 'День'),
            ('Час', 'Час'),
            ('Минута', 'Минута')
        ],
        verbose_name='Единица времени'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    def generate_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Item.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_slug()
        super(Item, self).save(*args, **kwargs)

    @property
    def price_with_symbol(self):
        return f'{self.price} ₽/{self.time_period} {self.time_period_unit}'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('-pub_date',)
