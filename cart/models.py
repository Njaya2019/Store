"""
Cart model.

This creates a cart database for products that are
about to be ordered.
"""

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


# This reciever updates the product quantity when a
# user adds the product to the Cart.
@receiver(post_save, sender=Cart, dispatch_uid="update_stock_count")
def update_stock(sender, instance, **kwargs):
    """Update numbers of products in the store."""
    if int(instance.product.product_amount) != 0:
        # if the difference of the quantity ordered and the stock is
        # a negative value, it leaves the product quantity as it was.
        # This int(str(instance.amount_to_order)) converts the django
        # safe string first to string then to an integer.
        if (int(instance.product.product_amount) -
                int(str(instance.amount_to_order))) < 0:
            instance.product.product_amount = instance.product.product_amount
        else:
            # Else updates the pdates the product amount
            instance.product.product_amount -=\
                int(str(instance.amount_to_order))
    else:
        # if the product quantity is 0, it leaves it as 0
        instance.product.product_amount = instance.product.product_amount
    # Saves the new product quantity in the store
    instance.product.save()
