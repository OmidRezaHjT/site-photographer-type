from django.urls import path
from accounts.views import *
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    path('login', custom_login_view, name='login'),
    path('signup',signup_view,name='signup'),
    path('logout/', custom_logout_view, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]