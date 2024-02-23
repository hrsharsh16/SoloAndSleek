from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom user model using built-in User and adding email field.
    """
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    USERNAME_FIELD = 'email'  # Set email as the username field for login
    REQUIRED_FIELDS = ['username']  # Remove unnecessary field requirements

    def __str__(self):
        return self.email
