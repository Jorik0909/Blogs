from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField


# Create your models here.

class Profile(models.Model):
    bio = models.CharField(max_length=500)
    avatar = models.ImageField(upload_to="avatars_media/", blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)