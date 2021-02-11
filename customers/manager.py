"""

A class extending the BaseUserModel.

This class will enable overriding, the default User model and
add extra fields.
"""
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """

    Custom UserManager.

    It's required to override the default django User,
    and add extra fields.
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """

        Create and save a User.

        With a given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            **extra_fields
        )

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        """

        Save the user.

        Sets the is_superuser field to false first before,
        saving the user.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """

        Save the superuser.

        Sets the is_superuser field to true first before,
        saving the user.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must have is_superuser=True.'
            )

        return self._create_user(email, password, **extra_fields)
