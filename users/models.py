from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=191)
