"""Users views"""

# Django
from django.contrib.auth import views as auth_views
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.urls.base import reverse_lazy

# Forms
from users import forms


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('users:dashboard')


class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = forms.ProfileForm
    success_url = reverse_lazy('users:dashboard')

    def form_valid(self, form):
        """Process after Form validation"""
        form.save()
        return super().form_valid(form)


def dashboardView(request):
    return render(request, 'users/dashboard.html')
