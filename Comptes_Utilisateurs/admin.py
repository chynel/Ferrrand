#coding: utf-8

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_superuser', 'is_client')
    list_filter = ('is_staff', 'is_superuser', 'is_client')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('noms','prenoms', 'sexe', 'DateNaiss', 'phone')}),
        ('Permissions', {
            'fields': ('is_active', 'is_client', 'is_staff', 'is_superuser', 'groups', 'user_permissions',),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
