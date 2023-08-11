from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'id', 'full_name',
                    'region', 'verification_code')
    search_fields = ('phone_number', 'full_name', 'region')
    ordering = ('date_joined', 'id')
