"""

Products view.

The view to add an item to the store.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from .serializers import ProductsSerializer
from .models import Products
from .utils import isAuthenticated, ProductNotFound


# Create your views here.
class ProductsView(APIView):
    """

    Products view.

    Adds, edit, view and delete products in the store.
    """

    authentication_classes = [SessionAuthentication, ]
    permission_classes = [isAuthenticated, ]

    def get_object(self, p_k):
        """Gets a product object"""
        try:
            return Products.objects.get(pk=p_k)
        except Products.DoesNotExist:
            raise ProductNotFound

    def post(self, request):
        """
        POST request.

        Adds a product to the store.
        """
        serializer = ProductsSerializer(
            data=request.data,
            context={'request': request}
        )
        # Checks if the request data is valid
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)

        # Returns an error if one the request data is invalid
        return Response(serializer.errors, status=400)
