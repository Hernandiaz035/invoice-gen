"""Users views"""

# Django
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls.base import reverse_lazy


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('users:dashboard')


def dashboardView(request):
    return render(request, 'users/dashboard.html')
