
"""

A custom user and proxy models to create users.

The proxy models are profiles of the users.
"""
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .manager import UserManager


# Create your models here.
class User(AbstractBaseUser,  PermissionsMixin):
    """

    A custom User model.

    Overrides the default User model by making 'email' as the,
    USERNAME_FIELD. PermissionsMixin makes the custom User,
    to use permissions if we are not need them.
    """

    email = models.EmailField(
        unique=True,
        max_length=255,
        blank=False,
    )

    firstname = models.CharField(
        max_length=20,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_superuser = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        default=timezone.now,
    )
    phone = PhoneNumberField(null=False, blank=False)

    # Changed the default field 'username' to 'email'.

    objects = UserManager()

    USERNAME_FIELD = 'email'
