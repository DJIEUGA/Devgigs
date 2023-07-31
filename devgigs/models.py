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
    website = models.TextField()
    description = models.TextField()
    company = models.CharField(max_length=255)
    tags = models.CharField(max_length=25)
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(blank=True, null=True, upload_to='images/')

    def serialize(self):
        return {
            "id": self.id,
            "author": self.user.username,
            "email": self.email,
            "title": self.title,
            "website": self.website,
            "description": self.description,
            "company": self.company,
            "tags": self.tags,
            "location": self.location,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p")
        }