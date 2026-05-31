from django.urls import path
from . import views
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path(
    'accounts/login/',
    views.smart_login,
    name='login'
),

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pro_slova/', views.pro_slova, name='pro_slova'),
    path('get-pro/', views.get_pro, name='get_pro'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path("payment/", views.payment),
    path("payment-done/", views.payment_done, name="payment_done"),
    path("search/", views.search, name="search"),
    path('trainer', views.trainer, name='trainer'),
    path("get-progress/", views.get_progress),
    path("save-progress/", views.save_progress),
    path(
    'accounts/logout/',
    auth_views.LogoutView.as_view(),
    name='logout'
),
]
