"""

Orders serializer.

This serializer validates the orders's fields first.
"""
from rest_framework import serializers
from .models import Orders
from cart.serializers import CartSerializer
from cart.models import Cart


class OrdersSerializer(serializers.ModelSerializer):
    """

    Model fields.

    Validates the corresponding model fields before,
    saving an order object.
    """

    cart = CartSerializer(many=True, read_only=True)
    user = serializers.CharField(
        source='user.firstname',
        read_only=True
    )

    class Meta:
        """The model and fields to be serialized."""

        model = Orders
        fields = [
            'id', 'user', 'date_ordered', 'cart',
        ]
        read_only_fields = ['user', 'date_ordered', 'cart']

    def create(self, validated_data):
        """
        Save order.

        Argument: validated_data. A dictionary of valid values.
        If all fields are valid this method will add the,
        order.
        """
        # gets the order if it exists already otherwise
        # it creates a new one.
        new_order, created = Orders.objects.get_or_create(
            user=self.context['request'].user,
        )
        # creates variable user
        user = self.context['request'].user
        # for each cart item related to the user and hasn't been
        # ordered yet, adds it to the new order and change the
        # ordered field from false to True, preventing the user
        # from ordering it gain from the cart
        for cart_item in Cart.objects.filter(user=user, ordered=False):
            new_order.cart.add(
                cart_item
            )
            cart_item.ordered = True
            cart_item.save()
        # saves the new order instance
        new_order.save()
        return new_order
