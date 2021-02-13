"""
Orders model.

This creates orders in database to ship the products
to their owners.
"""

import datetime
from django.conf import settings
from django.db import models
from cart.models import Cart

class Orders(models.Model):
    """Items in the store records."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    date_ordered = models.DateTimeField(
        default=datetime.datetime.today(),
        blank=False
    )

    cart = models.ManyToManyField(Cart)

    # shipped = models.BooleanField(
    #     default=False
    # )
    
