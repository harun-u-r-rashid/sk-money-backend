from django.contrib import admin

# Register your models here.
from .models import Package,Partner
#  Deposit, Withdraw, 


class PackageAdmin(admin.ModelAdmin):
    list_display = ["user", "id", "title"]


# class DepositAdmin(admin.ModelAdmin):
#     list_display = ["profile", "amount"]


# class WithdrawAdmin(admin.ModelAdmin):
#     list_display = ["profile", "amount"]


admin.site.register(Package, PackageAdmin)
# admin.site.register(Deposit, DepositAdmin)
# admin.site.register(Withdraw, WithdrawAdmin)
admin.site.register(Partner)