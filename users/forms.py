"""Users forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from django.forms.fields import EmailField
from users.models import Profile

style_attributes = {'class': 'form-control'}


class ProfileForm(forms.Form):
    """Signup form for user information."""

    username = forms.CharField(
        min_length=5,
        max_length=50,
        widget=forms.widgets.TextInput(attrs=style_attributes),
    )

    password = forms.CharField(
        max_length=100,
        widget=forms.widgets.PasswordInput(attrs=style_attributes),
    )
    password_confirm = forms.CharField(
        max_length=100,
        widget=forms.widgets.PasswordInput(attrs=style_attributes),
    )

    first_name = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.widgets.TextInput(attrs=style_attributes),
    )

    last_name = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.widgets.TextInput(attrs=style_attributes),
    )

    email = forms.CharField(
        min_length=6,
        max_length=80,
        widget=forms.widgets.EmailInput(attrs=style_attributes),
    )

    # abn = forms.CharField(
    #     max_length=20,
    #     blank=True,
    #     null=True
    # )
    # phone = forms.CharField(
    #     max_length=30,
    #     blank=True,
    #     null=True
    # )

    # address = forms.CharField(max_length=50)

    # bank_name = forms.CharField(max_length=30)
    # account_name = forms.CharField(max_length=30)
    # account_bsb = forms.CharField(max_length=10)
    # account_number = forms.CharField(max_length=20)

    def clean_username(self):
        """Username must be unique"""
        username = self.cleaned_data.get("username")
        username_used = User.objects.filter(username = username).exists()

        if username_used:
            raise forms.ValidationError(message="Username is already in use.")

        return username

    def clean(self):
        """Password Confirmation must match"""
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError(message="Password confirmation does not match")

        return cleaned_data

    def save(self):
        print(self.cleaned_data)
        data = self.cleaned_data
        data.pop("password_confirm")
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

