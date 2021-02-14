"""
Cart model.

This creates a cart database for products that are
about to be ordered.
"""

import datetime
from django.conf import settings
from django.db import models
from django.core.validators import (
    MinValueValidator, MaxValueValidator
)
from django.db.models.signals import post_save
from django.dispatch import receiver
from items.models import Products


class Cart(models.Model):
    """Model to store products to be ordered."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE
    )

    amount_to_order = models.IntegerField(
        blank=False,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100),
        ]
    )

    total_price = models.IntegerField(
        blank=False
    )

    ordered = models.BooleanField(
        default=False
    )

    def save(self, *args, **kwargs):
        """
        Override save.

        Updates the total price by multiplying
        the product quantity and it's price.
        """
        self.total_price = self.amount_to_order * self.product.product_price
        super().save(*args, **kwargs)


# This reciever updates the product stock number when a
# user adds the product to the Cart.
@receiver(post_save, sender=Cart, dispatch_uid="update_stock_count")
def update_stock(sender, instance, **kwargs):
    """Update numbers of products in the store."""
    if int(instance.product.product_amount) != 0:
        # if the difference of the amount ordered and the stock is
        # a negative value, it leaves the stock number as it was.
        if (instance.product.product_amount - instance.amount_to_order) < 0:
            instance.product.product_amount = instance.product.product_amount
        else:
            # Updates the stock
            instance.product.product_amount -= instance.amount_to_order
    else:
        # if stock is 0, it remains 0
        instance.product.product_amount = instance.product.product_amount
    instance.product.save()
