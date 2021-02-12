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

    def create(self, validated_data):
        """
        Save product.

        Argument: validated_data. A dictionary of valid values.
        If all fields are valid this method will add the,
        product.
        """
        new_product = Products.objects.create(
            user=self.context['request'].user,
            product_name=validated_data['product_name'],
            product_amount=validated_data['product_amount'],
        )

        return new_product