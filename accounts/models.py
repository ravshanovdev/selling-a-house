from django.db import models
from django.contrib.auth.models import AbstractUser


CUSTOM_CHOICE = (
    ('seller', 'Seller'),
    ('client', 'Client')
)


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=13)
    role = models.CharField(max_length=15, choices=CUSTOM_CHOICE)

    def __str__(self):
        return self.username


