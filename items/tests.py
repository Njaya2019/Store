"""
Tests Products view.

Tests values passed to the view.
"""

from json import loads
from rest_framework.test import APIClient
import pytest


@pytest.mark.django_db
class TestProductsView():
    """
    Products test.

    Tests for .
    """

    # A mock of the values to be passed the SignIn view.

    email = 'njayaandrew@yahoo.com'
    password = 'A1990n1$'
    product_name = 'Iphone 7'
    product_amount = 8

    # Initialises the client object
    client = APIClient()

    @pytest.fixture()
    def signUp_user(self):
        """
        Signup fixture.

        A fixture that signs up a user first
        """
        response = self.client.post(
            '/users/signup', {
                "email": self.email,
                "password": self.password,
                "confirm_password": self.password,
                "firstname": 'Andrew'
                }
        )

        data = response.content
        data = loads(data)

        # returns the user's id
        return data

    @pytest.fixture()
    def logs_user_in(self, signUp_user):
        """Log a user in."""
        response = self.client.post(
            '/users/signin', {
                "email": self.email,
                "password": self.password,
                }
        )

        data = response.content
        data = loads(data)

        return data

    def test_empty_productName(self, logs_user_in):
        """Tests an empty product name field."""
        response = self.client.post(
            '/products/add_product', {
                "product_name": '',
                "product_amount": self.product_amount,
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["product_name"][0] == "Please provide"\
            " product_name value"

    def test_empty_productAmount(self, logs_user_in):
        """Tests an empty product amount field."""
        response = self.client.post(
            '/products/add_product', {
                "product_name": self.product_name,
                "product_amount": '',
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["product_amount"][0] == "Please provide"\
            " product_amount value"

    def test_minValue_productAmount(self, logs_user_in):
        """Tests minimum value in product amount field."""
        response = self.client.post(
            '/products/add_product', {
                "product_name": self.product_name,
                "product_amount": -2,
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["product_amount"][0] == "Ensure this value is"\
            " greater than or equal to 0."

    def test_maxValue_productAmount(self, logs_user_in):
        """Tests maximum value in product amount field."""
        response = self.client.post(
            '/products/add_product', {
                "product_name": self.product_name,
                "product_amount": 100000,
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["product_amount"][0] == "Ensure this value is"\
            " less than or equal to 100."
