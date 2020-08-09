from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

from datetime import timedelta


class StrapUser(AbstractUser):
    age = models.PositiveIntegerField(
        verbose_name='Возраст', null=True
    )
    activation_key = models.CharField(max_length=256, blank=True)
    activation_key_expires = models.DateTimeField(
        default=(now() + timedelta(minutes=20))
    )

    @staticmethod
    def is_activation_key_expired(self):
        """Check activation key"""
        return now() > self.activation_key_expires
