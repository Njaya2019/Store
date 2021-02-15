"""
Tests Cart view.

Tests values passed to the view.
"""

from json import loads
from rest_framework.test import APIClient
import pytest


@pytest.mark.django_db
class TestCartView():
    """
    Cart test.

    Tests for validility of items passed to the,
    cart.
    """

    # A mock of the values to be passed the SignIn view.

    email = 'njayaandrew@yahoo.com'
    password = 'A1990n1$'
    product_name = 'Iphone 7'
    product_amount = 8
    product_price = 10

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
                "firstname": 'Andrew'
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
                "product_price": self.product_price,
                }
        )

        data = response.content
        data = loads(data)

        return data

    @pytest.fixture()
    def adds_another_product(self, login):
        """Fixture to add another product."""
        response = self.client.post(
            '/products/add_product', {
                "product_name": self.product_name,
                "product_amount": 0,
                "product_price": self.product_price,
                }
        )

        data = response.content
        data = loads(data)

        return data['id']

    def test_amountToOrder_invalidKey(self, adds_product):
        """Tests invalid amount to order field key."""
        response = self.client.post(
            '/cart/1/add_to_cart', {
                "product_name": self.product_name,
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["amount_to_order"][0] == "Please provide"\
            " amount_to_order as key"

    def test_amountToOrder_greaterThanStock(self, adds_product):
        """Tests if amount to order field is greater than stock."""
        response = self.client.post(
            '/cart/'+str(adds_product['id'])+'/add_to_cart', {
                "amount_to_order": 10,
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["error"] == "The amount you are"\
            " ordering is greater than the 8 items avaibale"

    def test_productToOrder_notFound(self, adds_product):
        """Tests if a product doesn't exist."""
        response = self.client.post(
            '/cart/10/add_to_cart', {
                "amount_to_order": 4,
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 404
        assert data["detail"] == "Sorry the product"\
            " doesn't exist"

    def test_productOut_ofStock(self, adds_another_product):
        """Tests if a product is out of stock."""
        response = self.client.post(
            '/cart/'+str(adds_another_product) +
            '/add_to_cart', {
                "amount_to_order": 4,
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["error"] == "Sorry we've ran out of stock "\
            "for this product"
