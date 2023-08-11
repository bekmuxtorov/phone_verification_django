from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(
        verbose_name='Phone number',
        max_length=20,
        unique=True,
        blank=True
    )
    full_name = models.CharField(
        verbose_name='Full name',
        max_length=50,
        blank=True
    )
    region = models.CharField(
        verbose_name='Region',
        max_length=50
    )
    is_staff = models.BooleanField(
        verbose_name="is staff",
        default=False
    )
    verification_code = models.IntegerField(
        verbose_name='Verification code',
        null=True,
        blank=True
    )
    is_phone_verified = models.BooleanField(
        default=False
    )
    date_joined = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.phone_number
