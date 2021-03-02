"""
Tests Orders view.

Tests values passed to the view.
"""

from json import loads
from rest_framework.test import APIClient
import pytest


@pytest.mark.django_db
class TestOrdersView():
    """
    Orders test.

    Tests for validility of the order.
    """

    # A mock of the values to be passed the SignIn view.

    email = 'njayaandrew@yahoo.com'
    password = 'A1990n1$'
    product_name = 'Iphone 7'
    product_amount = 8
    phone = '+254727645367'

    # Initialises the client object
    client = APIClient()

    @pytest.fixture()
    def signup(self):
        """
        Signup fixture.

        A fixture that signs up a user first
        """
        response = self.client.post(
            '/users/signup', {
                "email": self.email,
                "password": self.password,
                "confirm_password": self.password,
                "firstname": 'Andrew',
                "phone": self.phone
                }
        )

        data = response.content
        data = loads(data)

        # returns the user's id
        return data

    @pytest.fixture()
    def login(self, signup):
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

    @pytest.fixture()
    def adds_product(self, login):
        """Fixture to add a product."""
        response = self.client.post(
            '/products/add_product', {
                "product_name": self.product_name,
                "product_amount": self.product_amount,
                "product_price": 10,
                }
        )

        data = response.content
        data = loads(data)

        return data['id']

    @pytest.fixture()
    def adds_product_tocart(self, adds_product):
        """Fixture that adds a product to the cart."""
        response = self.client.post(
            '/cart/'+str(adds_product)+'/add_to_cart', {
                "amount_to_order": 4,
                }
        )

        data = response.content
        data = loads(data)

        return data

    def test_make_order(self, adds_product_tocart):
        """Tests an order has been successfully requested."""
        response = self.client.post(
            '/orders/make_order',
        )

        data = response.content
        data = loads(data)

        assert data['cart'][0]['product'] == 'Iphone 7'
        assert data['cart'][0]['amount_to_order'] == 4
