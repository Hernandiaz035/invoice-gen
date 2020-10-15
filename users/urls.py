"""Users URLs"""

# Django
from django.urls import path
from django.shortcuts import render
from django.http import request

# Models
from users import views

urlpatterns = [
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),

    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),

    path(
        route='logout/',
        view=views.auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        route='dashboard/',
        view=views.dashboardView,
        name='dashboard'
    ),
]
