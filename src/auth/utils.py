from django.conf import settings

from rest_framework import status
from rest_framework.response import Response
from rest_auth.serializers import JWTSerializer as DefaultJWTSerializer
from rest_auth.utils import import_callable


def jwt_response_payload_handler(token, user=None, request=None):
    """
    Returns the response data for both the login and refresh views.
    Override to return a custom response such as including the
    serialized representation of the User.

    Example:

    def jwt_response_payload_handler(token, user=None, request=None):
        return {
            'token': token,
            'user': UserSerializer(user, context={'request': request}).data
        }

    """
    serializers = getattr(settings, "REST_AUTH_SERIALIZERS", {})
    serializer_class = import_callable(
        serializers.get("JWT_SERIALIZER", DefaultJWTSerializer)
    )

    data = {"user": user, "token": token}
    serializer = serializer_class(instance=data, context={"request": request})
    return serializer.data
