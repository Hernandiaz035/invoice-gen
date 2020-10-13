"""Users URLs"""

# Django
from django.urls import path
from django.shortcuts import render
from django.http import request

# Models
from users import views

urlpatterns = [
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),

    path(
        route='dashboard/',
        view=views.dashboardView,
        name='dashboard'
    ),
]
