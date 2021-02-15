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
            'id', 'product_name', 'product_amount',
            'date_added', 'product_price',
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
            "product_price": {
                "error_messages": {
                    "required": "Please provide product price key",
                    "invalid": "Please provide product price value"
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
        # Checks if the product object already exists
        # if yes, it updates the product amount else,
        # creates
        obj_product, created = Products.objects.get_or_create(
            user=self.context['request'].user,
            product_name=validated_data['product_name'],
            defaults={
                'product_amount': validated_data['product_amount'],
                'product_price': validated_data['product_price'],
            }
        )
        if not created:
            # if amount added plus stock is greater than 100
            # return the old stock. 100 is the maximum number
            # of items allowed in the stock. Otherwise updates
            # the new product stock.
            if int(obj_product.product_amount)\
                    + int(validated_data['product_amount']) > 100:
                obj_product.product_amount = obj_product.product_amount
            else:
                obj_product.product_amount =\
                    int(obj_product.product_amount)\
                    + int(validated_data['product_amount'])
        # saves the product object
        obj_product.save()
        return obj_product
