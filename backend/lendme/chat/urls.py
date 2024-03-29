from django.contrib.auth.decorators import login_required
from django.urls import path

from chat import views

app_name = 'chat'

urlpatterns = [
    path('dialogs/', login_required(views.DialogsView.as_view()), name='dialogs'),
    path('dialogs/create/<int:user_id>', login_required(views.CreateDialogView.as_view()), name='create_dialog'),
    path('dialogs/<int:chat_id>', login_required(views.MessagesView.as_view()), name='messages'),
]
