"""

Orders serializer.

This serializer validates the orders's fields first.
"""
from rest_framework import serializers
from django.db.models import Sum
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
    phone = serializers.CharField(
        source='user.phone',
        read_only=True
    )
    # serializer method field, a read only field
    # which gets the total_price of the products
    # ordered
    the_total_price = serializers.SerializerMethodField()

    def get_the_total_price(self, obj):
        """Total price."""
        return obj.cart.all().aggregate(Sum('total_price'))

    class Meta:
        """The model and fields to be serialized."""

        model = Orders
        fields = [
            'id', 'user', 'phone', 'date_ordered', 'cart',
            'the_total_price',
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
            shipped=False
        )
        # creates variable user
        user = self.context['request'].user
        # for each cart item related to the user and hasn't been
        # ordered yet, adds it to the new order and change the
        # ordered field from false to True, preventing the user
        # from ordering it gain from the cart
        cart_objects = Cart.objects.filter(user=user, ordered=False)
        # If the user has items in the cart, ship the order else,
        # don't ship. This is to prevent shipping when a user
        # doesn't have items in the cart
        # if cart_objects:
        #     new_order.shipped = True
        # else:
        #     new_order.shipped = False
        for cart_item in cart_objects:
            new_order.cart.add(
                cart_item
            )
            cart_item.ordered = True
            cart_item.save()
        # saves the new order instance
        if cart_objects:
            new_order.shipped = True
        else:
            new_order.shipped = False
        new_order.save()
        return new_order
