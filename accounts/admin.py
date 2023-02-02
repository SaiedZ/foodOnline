from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User


class CustomUserAdmin(UserAdmin):
    """Custom user admin.

    Customize the admin panel for the custom user model.
    Make password field not editable.
    """

    list_display = (
        "email", "first_name", "last_name", "username", "role", "is_active"
    )
    ordering = ("-date_joined",)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, CustomUserAdmin)
