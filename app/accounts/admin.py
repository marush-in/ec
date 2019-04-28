from django.contrib import admin

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'name_kana', )
    list_per_page = 40


admin.site.register(CustomUser, CustomUserAdmin)
