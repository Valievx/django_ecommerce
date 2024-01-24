from django.contrib import admin

from catalog.models import Category, Item


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Админ-панель модели категорий """
    list_display = ('id', 'name', 'slug')
    prepopulated_fields: dict = {'slug': ('name',)}


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields: dict = {'slug': ('name',)}
