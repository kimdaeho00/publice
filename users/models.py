
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    name = models.CharField(
        max_length=20,
        blank=False,
    )
    email = models.EmailField(
        max_length=50,
        blank=False,
    )
    password = models.CharField(
        max_length=10,
        blank=False,
    )
    nickname = models.CharField(max_length=10,
        blank=False,
    )
    phone_number = models.CharField(max_length=14,blank=True)

    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name