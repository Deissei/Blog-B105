from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=13,
        unique=True,
        verbose_name='Phone Number',
    )
    is_person_code = models.CharField(
        max_length=6,
        unique=True,
        verbose_name='Is Person Code',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username
