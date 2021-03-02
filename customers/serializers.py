"""

Signup serializer.

This serializer validates registration fields first,
before registering a user.
"""
from rest_framework import serializers
from .models import User
from .validators import FieldValidator


class SignUpSerializer(serializers.ModelSerializer):
    """

    Model fields.

    Validates the corresponding model fields before,
    saving the user object.
    """

    confirm_password = serializers.CharField(
        error_messages={
            "required": "Please provide confirm password key",
            "blank": "Please provide confirm password value"
        },
        write_only=True
    )

    class Meta:
        """The model and fields to be serialized."""

        model = User
        fields = [
            'id', 'email', 'firstname',
            'password', 'confirm_password', 'phone'
        ]
        extra_kwargs = {
            "password": {
                "error_messages": {
                    "required": "Please provide password as key",
                    "blank": "Please provide password value"
                },
                "write_only": True
            },
            "email": {
                "error_messages": {
                    "required": "Please provide email key",
                    "blank": "Please provide email value"
                }
            },
            "firstname": {
                "error_messages": {
                    "required": "Please provide firstname key",
                    "blank": "Please provide firstname value"
                }
            },
            "phone": {
                "error_messages": {
                    "required": "Please provide a phone number key",
                    "blank": "Please provide a phone number"
                }
            },
        }

    def validate(self, data):
        """
        Argument: data.

        A dictionary that has key value pair of all fields,
        passed.
        """
        # escapes the field string values first
        data = FieldValidator.escaping_characters(**data)
        # The rest validate individual field values.
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(
                "The password and confirm password do not match"
            )

        strong_password = FieldValidator.is_strong_password(
            data['password']
        )
        if not strong_password:
            raise serializers.ValidationError(
                "The password must contain atleast one uppercase,"
                " lowercase, a number, special character '$%^&'"
                " and should be eight character long"
            )

        valid_firstname = FieldValidator.is_valid_fullname(
            data['firstname']
        )
        if not valid_firstname:
            raise serializers.ValidationError(
                "Please provide the firstname with first letter"
                " as an Uppercase followed by lowercase letters"
            )
        return data

    def create(self, validated_data):
        """
        Save user.

        Argument: validated_data. A dictionary of valid values.
        If all fields are valid this method will add the,
        user's information to the database.
        """
        new_user = User.objects.create_user(
            email=validated_data['email'],
            firstname=validated_data['firstname'],
            phone=validated_data['phone'],
            password=validated_data['password'],
        )

        return new_user
