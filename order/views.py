"""

Orders view.

This view makes an order.
"""
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from django.db.models import Sum
from .serializers import OrdersSerializer
from items.utils import isAuthenticated
from cart.models import Cart


# Create your views here.
class OrdersView(APIView):
    """

    Orders view.

    Makes an order.
    """

    authentication_classes = [SessionAuthentication, ]
    permission_classes = [isAuthenticated, ]

    def post(self, request):
        """
        POST request.

        Creates an order.
        """
        # Passes the data to the serializer
        serializer = OrdersSerializer(
            data=request.data,
            context={
                'request': request,
            }
        )
        # Checks if the request data is valid
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # gets the sum of the total price in the cart
            total_amount = Cart.objects.all().filter(
                user=request.user,
            ).aggregate(Sum('total_price'))
            # converts the date string to date object
            date_obj = datetime.datetime.strptime(
                serializer.data['date_ordered'],
                '%Y-%m-%dT%I:%M:%S.%fZ'
            )
            # converts it back to string in a more good format
            date_ordered = date_obj.strftime(
                    '%d-%m-%y %H:%M:%S %p'
            )
            # grabs the order id
            order_id = serializer.data['id']
            # grabs the user ordering
            customer_name = serializer.data['user']
            # gets the cart items to be ordered
            cart_items = serializer.data['cart']
            # initialises a list with two items, customer
            # name and the order id
            product_amount = [
                'order serial No. '+str(order_id) +
                ', customer name: '+str(customer_name),
                'date ordered: '+date_ordered,
                '---------------------',
                'Pdct     Qty     tlt',
                '----------------------'
            ]
            # list comprehension that joins the product and
            # amount in one string
            ordered_cart_items = [
                item['product']+"\t" +
                str(item['amount_to_order'])+"\t" +
                str(item['total_price']) for
                item in cart_items
            ]
            # adds the items to the product_amount list
            product_amount.extend(ordered_cart_items)
            # appends the total amount of all products
            # as a string
            product_amount.extend([
                '---------------------',
                'total\t\t'+str(
                    total_amount['total_price__sum']
                )
            ])
            # Joins the list of the products and their
            # quantity in a single string with a new
            # line in the string after each element
            # in the array
            receit = '\n'.join(
                product_amount
            )
            print(receit)
            return Response(serializer.data, status=201)

        # Returns an error if one the request data is invalid
        return Response(serializer.errors, status=400)
