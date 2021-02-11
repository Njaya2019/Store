"""

Signup and Signin.

These are views, where users can register,
and are authenticated before they access the,
services.
"""
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SignUpSerializer


# Create your views here.
class SignUp(APIView):
    """

    Signup view.

    Users are registered in this view.
    """

    def post(self, request):
        """
        POST request.

        This registers a user with the platform.
        """
        serializer = SignUpSerializer(data=request.data)
        # Checks if the request data is valid
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)

        # Returns an error if one the request data is invalid
        return Response(serializer.errors, status=400)


class SignIn(APIView):
    """

    Signin view.

    Authenticates users before accessing the protected views.
    """

    def post(self, request):
        """
        POST request.

        This authenicates users.
        """
        # Converts the signup form QueryDict to a dictionary.
        signup_formData = request.POST.dict()

        # checks if email and password keys exists in the,
        # form data dictionary.
        if 'email' not in signup_formData or 'password' not in signup_formData:
            return Response(
                {
                    'error': 'Please provide email and password keys'
                },
                status=400
            )
        else:
            if not signup_formData['email'] or not signup_formData['password']:
                return Response(
                    {
                        'error': 'Please provide email and password values'
                    },
                    status=400
                )
            else:
                user = authenticate(
                    request,
                    email=request.POST['email'],
                    password=request.POST['password']
                )
                if user is not None:
                    login(request, user)
                    return Response(
                        {
                            "message": "logged in"
                        },
                        status=200
                    )
                else:
                    return Response(
                        {
                            "error": "Please provide correct email and"
                            " password"
                        },
                        status=403
                    )
