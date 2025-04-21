from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# Custom user model extending AbstractUser
class CustomUser(AbstractUser):
  # add additional fields in here
  bio = models.TextField(blank=True, null=True)