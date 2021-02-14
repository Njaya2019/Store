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

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    product_name = models.CharField(
        max_length=30,
        blank=False,
    )
    product_price = models.IntegerField(
        blank=False,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(1000000),
        ]
    )

    product_amount = models.IntegerField(
        blank=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ]
    )
    date_added = models.DateField(
        default=datetime.date.today,
        blank=False
    )
