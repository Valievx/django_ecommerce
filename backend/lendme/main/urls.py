from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_items/', views.get_items, name='get_items'),
]
