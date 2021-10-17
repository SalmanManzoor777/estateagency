from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_owner = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    name = models.CharField(max_length=200, default='xyz')
    email = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=100, blank=False, default=12345)

class Vistor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=256, blank=False)
    phone = models.IntegerField()

    def __str__(self):
        return self.user.username


class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
