"""

Orders view.

This view makes an order.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from .serializers import OrdersSerializer
from items.utils import isAuthenticated


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
            return Response(serializer.data, status=201)

        # Returns an error if one the request data is invalid
        return Response(serializer.errors, status=400)

