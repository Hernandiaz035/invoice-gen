"""Users views"""

# Django
from django.contrib.auth import views as auth_views
from django.shortcuts import render


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    success_url = 'users/dashboard.html'


def dashboardView(request):
    return render(request, 'users/dashboard.html')
