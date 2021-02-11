"""

Products serializer.

This serializer validates the product's fields first,
before adding it to the store.
"""
from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
    """

    Model fields.

    Validates the corresponding model fields before,
    saving the Product object.
    """

    class Meta:
        """The model and fields to be serialized."""

        model = Products
        fields = [
            'product_name', 'product_amount',
            'date_added',
        ]
        extra_kwargs = {
            "product_name": {
                "error_messages": {
                    "required": "Please provide product_name as key",
                    "blank": "Please provide product_name value"
                }
            },
            "product_amount": {
                "error_messages": {
                    "required": "Please provide product_amount key",
                    "invalid": "Please provide product_amount value"
                }
            },
        }