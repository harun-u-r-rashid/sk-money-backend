from django.contrib import admin

# Register your models here.
from . import models

#  Deposit, Withdraw,


class PackageAdmin(admin.ModelAdmin):
    list_display = ["title", "price"]


class DepositAdmin(admin.ModelAdmin):
    list_display = ["user", "status","package_name",  "transaction_id", "amount", "send_number"]


class WithdrawAdmin(admin.ModelAdmin):
    list_display = ["user", "status",  "amount"]


admin.site.register(models.Package, PackageAdmin)
admin.site.register(models.Deposit, DepositAdmin)
admin.site.register(models.Withdraw, WithdrawAdmin)
admin.site.register(models.Partner)
admin.site.register(models.SliderImage)


# Celery
