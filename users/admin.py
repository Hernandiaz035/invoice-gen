"""User admin Profile"""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


class ProfileInline(admin.StackedInline):
    """Profile InLine Admin Form"""
    model = Profile
    verbose_name_plural = 'Profile'
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
