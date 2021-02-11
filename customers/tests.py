"""
Test SignUp view.

Tests values passed to the view.
"""

from json import loads
from rest_framework.test import APIClient
import pytest


# @pytest.mark.django_db used to mark a test function as,
# requiring a database. It will ensure a database is setup,
# correctly for the test. Each test will run in it's own,
# transaction and will be rolled back at the end of the test.
# In order for a test to have access to the database it must,
# be marked with either django_db() mark or request one of,
# the db, transactional_db() or django_db_reset_sequences,
# fixtures. Otherwise the test will fail while trying to,
# access the database.
@pytest.mark.django_db
class TestUsersSignUp():
    """
    SignUp test.

    Tests email, password, confirm password
    and firstname fields.
    """

    # A mock of the values to be passed the SignUp view.

    email = 'njayaandrew@gmail.com'
    password = 'A1990n1$'
    confirm_password = 'A1990n1$'
    firstname = 'Andrew'

    # Initialises the client object
    client = APIClient()

    def test_empty_email(self):
        """Tests an empty email field."""
        response = self.client.post(
            '/users/signup', {
                "email": '',
                "password": self.password,
                "confirm_password": self.confirm_password,
                "firstname": self.firstname
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["email"][0] == "Please provide email value"

    def test_empty_password(self):
        """Tests an empty password field."""
        response = self.client.post(
            '/users/signup', {
                "email": self.email,
                "password": '',
                "confirm_password": self.confirm_password,
                "firstname": self.firstname
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["password"][0] == "Please provide password value"

    def test_empty_confirmPassword(self):
        """Tests an empty confirm password field."""
        response = self.client.post(
            '/users/signup', {
                "email": self.email,
                "password": self.password,
                "confirm_password": '',
                "firstname": self.firstname
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["confirm_password"][0] == "Please provide confirm "\
            "password value"

    def test_empty_firstname(self):
        """Tests an empty firstname field."""
        response = self.client.post(
            '/users/signup', {
                "email": self.email,
                "password": self.password,
                "confirm_password": self.confirm_password,
                "firstname": ''
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["firstname"][0] == "Please provide"\
            " firstname value"

    def test_password_dontMatch(self):
        """Tests a password match."""
        response = self.client.post(
            '/users/signup', {
                "email": self.email,
                "password": self.password,
                "confirm_password": 'n1990A1&',
                "firstname": self.firstname
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["non_field_errors"][0] == "The password and confirm"\
            " password do not match"

    def test_strongPassword(self):
        """Tests a strong password value."""
        response = self.client.post(
            '/users/signup', {
                "email": self.email,
                "password": 'password',
                "confirm_password": 'password',
                "firstname": self.firstname
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["non_field_errors"][0] == "The password must contain"\
            " atleast one uppercase, lowercase, a"\
            " number, special character '$%^&'"\
            " and should be eight character long"

    def test_emailKey_doNotExist(self):
        """Tests for email key field."""
        response = self.client.post(
            '/users/signup', {
                "password": self.password,
                "confirm_password": self.confirm_password,
                "firstname": self.firstname
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["email"][0] == "Please provide email key"

    def test_passwordKey_doNotExist(self):
        """Tests for password key field."""
        response = self.client.post(
            '/users/signup', {
                "email": self.email,
                "confirm_password": self.confirm_password,
                "firstname": self.firstname
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["password"][0] == "Please provide password as key"

    def test_confirmPasswordKey_doNotExist(self):
        """Tests for confirm password key field."""
        response = self.client.post(
            '/users/signup', {
                "email": self.email,
                'password': self.password,
                "firstname": self.firstname
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["confirm_password"][0] == "Please provide confirm"\
            " password key"

    def test_firstnameKey_doNotExist(self):
        """Tests for type of user key field."""
        response = self.client.post(
            '/users/signup', {
                "email": self.email,
                'password': self.password,
                'confirm_password': self.confirm_password
                }
        )

        data = response.content
        data = loads(data)

        assert response.status_code == 400
        assert data["firstname"][0] == "Please provide firstname key"

