from django.db import models
from appAuth.models import User
from .constants import STATUS



class Package(models.Model):
        # user = models.ForeignKey(User, on_delete=models.CASCADE)
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


class SliderImage(models.Model):
        image1 = models.ImageField(upload_to="slider_image_folder")
        image2 = models.ImageField(upload_to="slider_image_folder")
        image3 = models.ImageField(upload_to="slider_image_folder")


        def __str__(self):
                return f"{self.id}"
        
        


class Deposit(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        amount = models.IntegerField(default=0)
        tran_id = models.CharField(unique=True, max_length=100)
        status = models.CharField(max_length=30, choices=STATUS, default="PENDING")
        created_at = models.DateTimeField(auto_now_add=True)
        profit_start_date = models.DateField(null=True, blank=True)


        def __str__(self):
                return f"{self.user} ===== {self.amount}"
        


class Withdraw(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        amount = models.IntegerField(default=0)
        b_number = models.CharField(max_length=20, blank=True, null=True)
        msg = models.CharField(max_length=255)
        status = models.CharField(max_length=30, choices=STATUS, default="PENDING")
        

        def __str__(self):
                return f"{self.user} ===== {self.amount}"

