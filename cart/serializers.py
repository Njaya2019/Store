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
            'amount_to_order', 'total_price'
        ]
        read_only_fields = ['user', 'product', 'total_price']
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
        # gets the cart object if it exists otherwise creates
        # new cart object and returns it.
        new_item_obj, created = Cart.objects.get_or_create(
            user=self.context['request'].user,
            product=self.context['product_object'],
            ordered=False,
            defaults={'amount_to_order': validated_data['amount_to_order']}
        )
        # created is a boolean which checks if the new object
        # was added or not. if it wasn't means the product is in
        # the cart model and if it hasn't been ordered yet
        # increament the product quantity to be ordered.
        if not created:
            # returns the old product quantity
            if int(new_item_obj.amount_to_order) +\
                    int(validated_data['amount_to_order']) > 100:
                new_item_obj.amount_to_order =\
                    new_item_obj.amount_to_order
            else:
                # updates the new product quantity to be
                # ordered in the cart
                new_item_obj.amount_to_order =\
                    int(new_item_obj.amount_to_order)\
                    + int(validated_data['amount_to_order'])
        new_item_obj.save()
        return new_item_obj
