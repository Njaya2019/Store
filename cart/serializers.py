"""

Cart serializer.

This serializer validates the cart's fields first,
before adding it to the store.
"""
from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    """

    Model fields.

    Validates the corresponding model fields before,
    saving a Cart object.
    """

    user = serializers.CharField(
        source='user.firstname',
        read_only=True
    )
    product = serializers.CharField(
        source='product.product_name',
        read_only=True
    )
    class Meta:
        """The model and fields to be serialized."""

        model = Cart
        fields = [
            'id', 'user', 'product',
            'amount_to_order',
        ]
        read_only_fields = ['user', 'product']
        depth = 1
        extra_kwargs = {
            "amount_to_order": {
                "error_messages": {
                    "required": "Please provide amount_to_order as key",
                    "blank": "Please provide amount_to_order value",
                    "invalid": "Please provide a valid integer"
                }
            },
        }
    
    def create(self, validated_data):
        """
        Save product to cart.

        Argument: validated_data. A dictionary of valid values.
        If all fields are valid this method will add the,
        product to the cart.
        """
        self.context['product_object'].product_amount  -= validated_data['amount_to_order']
        new_item = Cart.objects.create(
            user=self.context['request'].user,
            product=self.context['product_object'],
            amount_to_order=validated_data['amount_to_order'],
        )

        return new_item
