from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_items/', views.get_items, name='get_items'),
    path('additem/', views.additem, name='additem'),
    path('edititem/<int:item_id>/', views.edit_item, name='edit_item'),
    path('deleteitem/<int:item_id>/', views.delete_item, name='delete_item'),
]
