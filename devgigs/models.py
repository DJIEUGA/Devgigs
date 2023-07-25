from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Listing(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="creator")
    email = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)
    tags = models.CharField(max_length=25)
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(blank=True)