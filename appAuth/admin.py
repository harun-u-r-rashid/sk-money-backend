from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
        list_display = ['email', 'username', 'profit', 'balance','bkash_number','id']

# class ProfileAdmin(admin.ModelAdmin):
#         list_display = ['id']

admin.site.register(User, UserAdmin)

# admin.site.register(Profile, ProfileAdmin)
