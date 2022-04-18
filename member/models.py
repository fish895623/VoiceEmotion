from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    favorite = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
