from django.contrib import admin

# Register your models here.
from . import models

#  Deposit, Withdraw,


class PackageAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]


class DepositAdmin(admin.ModelAdmin):
    list_display = ["id", "status", "user", "tran_id", "amount"]


class WithdrawAdmin(admin.ModelAdmin):
    list_display = ["id", "status", "user", "amount"]


admin.site.register(models.Package, PackageAdmin)
admin.site.register(models.Deposit, DepositAdmin)
admin.site.register(models.Withdraw, WithdrawAdmin)
admin.site.register(models.Partner)
admin.site.register(models.SliderImage)


# Celery
