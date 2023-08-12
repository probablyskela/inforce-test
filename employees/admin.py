from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import EmployeeCreationForm, EmployeeChangeForm
from .models import Employee


class EmployeeAdmin(UserAdmin):
    add_form = EmployeeCreationForm
    form = EmployeeChangeForm
    model = Employee

    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_superuser",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "first_name",
        "last_name",
        "is_superuser",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password",
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Employee, EmployeeAdmin)
