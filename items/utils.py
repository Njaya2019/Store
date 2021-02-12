"""
Authentication and Exceptions.

These are utility classes to override
exception messages in the views.
"""

from rest_framework.exceptions import APIException
from rest_framework.permissions import BasePermission


class UserNotFound(APIException):
    """
    User exists.

    This exception provide a good custom error message,
    when a user is not found.
    """

    status_code = 404
    default_detail = 'Sorry the user with the id dosen\'t exist'
    default_code = "user_not_found"


class AuthenticationException(APIException):
    """
    Authentication exception.

    This exception provide a good custom error message,
    when a user has bee not authenticated.
    """

    status_code = 401
    default_detail = 'Please login first to add a product'
    default_code = "user_resource_denied"


class isAuthenticated(BasePermission):
    """Authentication."""

    def has_permission(self, request, view):
        """
        User authenticated.

        Raises an authentication error if the user is not
        authenticated
        """
        if not request.user.is_authenticated:
            raise AuthenticationException
        return True


class ProductNotFound(APIException):
    """
    Product exists.

    This exception provide a good custom error message,
    when a product doesn't exist.
    """

    status_code = 404
    default_detail = 'Sorry the product doesn\'t exist'
    default_code = "product_not_found"
