from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path
from django.urls import reverse_lazy


from users import views

app_name = 'users'


urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile_edit, name='profile_edit'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='users/password_change_form.html',
            success_url=reverse_lazy('users:password_change_done')),
        name='password_change'
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html'),
        name='password_change_done'
    ),
    path(
        'password-reset/',
        views.UserForgotPasswordView.as_view(),
        name='password_reset'
    ),
    path(
        'set-new-password/<uidb64>/<token>/',
        views.UserPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path('create_review/<int:seller_id>/', views.create_review, name='create_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('reviews/<int:user_id>/', views.my_reviews, name='reviews'),
]
