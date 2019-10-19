from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

@admin.register(User)
class AdminUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'phone', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name','email')

@admin.register(UserProfile)
class AdminUserProfile(admin.ModelAdmin):
    pass
