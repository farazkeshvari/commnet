from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUSerAdmin(admin.ModelAdmin):
    list_display = ["username", "email"]
