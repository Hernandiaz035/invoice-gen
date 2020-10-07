"""Users models"""

# Django
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    """Profile model.
    Proxy that extends user information."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    abn = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    phone = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    address = models.CharField(max_length=50)

    bank_name = models.CharField(max_length=30)
    account_name = models.CharField(max_length=30)
    account_bsb = models.CharField(max_length=10)
    account_number = models.CharField(max_length=20)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username