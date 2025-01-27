from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db.models.signals import post_save
from rest_framework_simplejwt.tokens import RefreshToken


class AccountManager(BaseUserManager):
    def create_user(
        self,
        username,
        full_name,
        email,
        password=None,
        image=None,
        balance=0,
        profit=0,
    ):
        if not email:
            raise ValueError("User must have and email address")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            full_name=full_name,
            image=image,
            balance=balance,
            profit=profit,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, full_name, email, password, image=None, balance=0, profit=0
    ):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            full_name=full_name,
            password=password,
            image=image,
            balance=balance,
            profit = 0
        )

        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=30)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    bkash_number = models.CharField(max_length=20, default="01*********")
    balance = models.IntegerField(default=100)
    profit = models.IntegerField(default=0)
    image = models.ImageField(upload_to="user_image_folder", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    otp = models.CharField(max_length=100, null=True, blank=True)
    refresh_token = models.CharField(max_length=1000, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "full_name"]
    objects = AccountManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        refresh_payload = refresh.payload
        refresh_payload["is_active"] = self.is_active
        refresh_payload["is_superuser"] = self.is_superadmin
        return {"refresh": str(refresh), "access": str(refresh.access_token)}

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class OneTimePassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.user.username}"


