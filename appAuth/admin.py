from django.contrib import admin

from .models import User, Profile

class UserAdmin(admin.ModelAdmin):
        list_display = ['id', 'username', 'email']

class ProfileAdmin(admin.ModelAdmin):
        list_display = ['id']

admin.site.register(User, UserAdmin)

admin.site.register(Profile, ProfileAdmin)
