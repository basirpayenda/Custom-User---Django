from django.contrib import admin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

CustomUser = get_user_model()


class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'phoneNumber', 'jobTitle', 'zipCode', 'degree', 'password1', 'password2')}
         ),
    )


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'phoneNumber']


admin.site.register(CustomUser, CustomUserAdmin)
