from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

# Create your models here.
User = get_user_model()

class Pwdlist(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username