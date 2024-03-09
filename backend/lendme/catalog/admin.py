from django.contrib import admin

from catalog.models import Category, Item, ItemImage, Favorite


class ItemImageAdmin(admin.StackedInline):
    model = ItemImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Админ-панель модели категорий """
    list_display = ('id', 'name', 'slug')
    prepopulated_fields: dict = {'slug': ('name',)}


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """ Админ-панель модели товара """
    prepopulated_fields: dict = {'slug': ('name',)}
    inlines = [ItemImageAdmin]


@admin.register(ItemImage)
class ItemImage(admin.ModelAdmin):
    pass


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    model = Favorite
    list_display = ('id', 'item', 'user')
