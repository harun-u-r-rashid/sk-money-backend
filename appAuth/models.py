
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models.signals import post_save
from rest_framework_simplejwt.tokens import RefreshToken


class AccountManager(BaseUserManager):
    def create_user(self, username, full_name,  email, password=None):
        if not email:
            raise ValueError("User must have and email address")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            full_name=full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, full_name, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username=username,
            full_name = full_name,
            password=password,
        )

        user.is_active=True
        user.is_admin = True
        user.is_staff=True
        user.is_superadmin = True
        user.save(using=self._db)

        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=30)
    full_name = models.CharField( max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
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
        return {"refresh": str(refresh), "access": str(refresh.access_token)}
    

    def has_perm(self, perm, obj=None):
        return self.is_admin
         
    def has_module_perms(self, add_label):
        return True

    def save(self, *args, **kwargs):
        email_username, _ = self.email.split("@")

        if self.full_name == "" or self.full_name == None:
            self.full_name = email_username
        if self.username == "" or self.username == None:
            self.username = email_username
        super(User, self).save(*args, **kwargs)


class OneTimePassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.user.username}"
    


    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="user_folder",  null=True, blank=True
    )
    balance = models.IntegerField(default=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.full_name)
            



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
