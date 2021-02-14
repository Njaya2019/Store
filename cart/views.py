"""

Cart view.

This view adds a product to the cart.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from .serializers import CartSerializer
from items.utils import isAuthenticated
from items.views import ProductsView


# Create your views here.
class CartView(APIView):
    """

    Products view.

    Adds, edit, view and delete products in the cart.
    """

    authentication_classes = [SessionAuthentication, ]
    permission_classes = [isAuthenticated, ]

    product_view_object = ProductsView()

    def post(self, request, product_id):
        """
        POST request.

        Adds a product in a cart.
        """
        product_object = self.product_view_object.get_object(
            product_id
        )
        # Gets the form data
        prdct_amnt_Dict = request.POST.dict()
        # Checks if the amount_to_order key is in the,
        # form data.
        if 'amount_to_order' in prdct_amnt_Dict:
            # Ensures users to only order item amount
            # thats available in the store.
            if int(product_object.product_amount) == 0:
                return Response(
                    {
                        "error": "Sorry we've ran out of stock "
                        "for this product"
                    },
                    status=400
                )
            elif int(prdct_amnt_Dict['amount_to_order'])\
                    > int(product_object.product_amount):
                return Response(
                    {
                        "error": "The amount you are ordering is"
                        " greater than the {} items avaibale"
                        .format(product_object.product_amount)
                    },
                    status=400
                )
        # Passes the data to the serializer
        serializer = CartSerializer(
            data=request.data,
            context={
                'request': request,
                'product_object': product_object
            }
        )
        # Checks if the request data is valid
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)

        # Returns an error if one the request data is invalid
        return Response(serializer.errors, status=400)
