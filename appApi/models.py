from django.db import models
from appAuth.models import Profile
from .constants import STATUS



class Package(models.Model):
        profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
        title = models.CharField(unique=True, max_length=30)
        price = models.IntegerField(default=0)
        description = models.TextField(max_length=255)
        image = models.ImageField(upload_to="package_folder", blank=True, null=True)

        def __str__(self):
                return f"{self.title}"
        


class Partner(models.Model):
        image = models.ImageField(upload_to="partner_folder", blank=True, null=True)
        name = models.CharField(max_length=20)

        def __str__(self):
                return f"{self.name}"

class Deposit(models.Model):
        profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
        amount = models.IntegerField(default=0)
        tran_id = models.CharField(unique=True, max_length=100)
        status = models.CharField(max_length=30, choices=STATUS, default="PENDING")
        

        def __str__(self):
                return f"{self.profile} ===== {self.amount}"
        


class Withdraw(models.Model):
        profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
        amount = models.IntegerField(default=0)
        tran_id = models.CharField(unique=True, max_length=100)
        status = models.CharField(max_length=30, choices=STATUS, default="PENDING")
        

        def __str__(self):
                return f"{self.profile} ===== {self.amount}"

