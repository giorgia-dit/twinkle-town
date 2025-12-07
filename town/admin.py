from django.contrib import admin
from .models import User, House
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    ...


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'slug', 'name', 'owner')
    prepopulated_fields = {'slug': ['name']}
