from django.urls import path

from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('search/', views.search_items, name='search'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]
