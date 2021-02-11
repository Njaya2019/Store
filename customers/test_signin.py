"""
Test SignIn view.

Tests values passed to the view.
"""

from json import loads
from rest_framework.test import APIClient
import pytest


@pytest.mark.django_db
class TestUsersSignIn():
    """
    SignIn test.

    Tests email and password fields.
    """

    # A mock of the values to be passed the SignIn view.

    email = 'njayaandrew@gmail.com'
    password = 'A1990n1$'

    # Initialises the client object
    client = APIClient()

    @pytest.fixture()
    def signUp_user(self):
        """
        Signup fixture.

        A fixture that signs up a user
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

    def test_empty_email(self):
        """Tests an empty email field."""
        response = self.client.post(
            '/users/signin', {
                "email": '',
                "password": self.password,
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["error"] == 'Please provide email and password values'

    def test_empty_password(self):
        """Tests an empty password field."""
        response = self.client.post(
            '/users/signin', {
                "email": self.email,
                "password": '',
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["error"] == 'Please provide email and password values'

    def test_email_key(self):
        """Tests email key field."""
        response = self.client.post(
            '/users/signin', {
                "password": self.password
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["error"] == 'Please provide email and password keys'

    def test_password_key(self):
        """Tests password key field."""
        response = self.client.post(
            '/users/signin', {
                "email": self.email
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["error"] == 'Please provide email and password keys'

    def test_IncorrectPassword(self, signUp_user):
        """Tests for incorrect password."""
        response = self.client.post(
            '/users/signin', {
                "email": self.email,
                "password": 'a1990n'
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 403
        assert data["error"] == "Please provide correct email and password"

    def test_IncorrectEmail(self, signUp_user):
        """Tests for incorrect email."""
        response = self.client.post(
            '/users/signin', {
                "email": 'njayaandrew@yahoo.com',
                "password": self.password
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 403
        assert data["error"] == "Please provide correct email and password"

    def test_correct_EmailAndPassword(self, signUp_user):
        """Tests a successfully login."""
        response = self.client.post(
            '/users/signin', {
                "email": self.email,
                "password": self.password
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 200
        assert data["message"] == "logged in"
