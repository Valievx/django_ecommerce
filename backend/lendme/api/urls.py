from django.urls import path
from . import views

urlpatterns = [
    path('api/load_more/', views.load_more, name='load_more'),
]