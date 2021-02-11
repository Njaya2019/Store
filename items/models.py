"""
Products model.

This creates items database for items in the
store.
"""

import datetime
from django.core.validators import (
    MinValueValidator, MaxValueValidator
)
from django.conf import settings
from django.db import models


class Products(models.Model):
    """Items in the store records."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True
    )

    product_name = models.CharField(
        max_length=30,
        blank=False,
    )

    product_amount = models.IntegerField(
        blank=False,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100),
        ]
    )

    date_added = models.DateField(
        default=datetime.date.today,
        blank=False
    )
