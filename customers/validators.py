"""
Form fields validators.

Classes with methods that validate, input text,
integers est.
"""
import re


class FieldValidator:
    """
    The validator.

    methods that do the validation.
    """

    @staticmethod
    def is_strong_password(password_value):
        """
        Validate password.

        Makes a user to create a strong password.
        """
        uppercase_pattern = re.compile(r'[A-Z]+')
        lowercase_pattern = re.compile(r'[a-z]+')
        digits_pattern = re.compile(r'[0-9]+')
        special_chars_pattern = re.compile(r'[\W]+')

        if len(password_value) < 8:
            return False
        elif not uppercase_pattern.search(password_value):
            return False
        elif not lowercase_pattern.search(password_value):
            return False
        elif not digits_pattern.search(password_value):
            return False
        elif not special_chars_pattern.search(password_value):
            return False
        else:
            return True
    
    @staticmethod
    def is_valid_fullname(name):
        """
        Validates name.

        Makes a user to create a valid name.
        """
        name_pattern = re.compile(r'[A-Z]{1}[a-z]+')
        if not name_pattern.fullmatch(name):
            return False
        return True