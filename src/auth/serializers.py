from rest_framework import serializers
from rest_auth.serializers import (
    LoginSerializer as BaseLoginSerializer,
    JWTSerializer as BaseJWTSerializer)
from rest_auth.registration.serializers import \
    RegisterSerializer as BaseRegisterSerializer

from rest_framework_simplejwt.views import TokenObtainPairView

class LoginSerializer(BaseLoginSerializer):
    username = None


class RegisterSerializer(BaseRegisterSerializer):
    username = None
    first_name = serializers.CharField(required=True, max_length=255, allow_blank=False)
    last_name = serializers.CharField(required=True, max_length=255, allow_blank=False)

    def get_cleaned_data(self):
        return {
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "password1": self.validated_data.get("password1", ""),
        }

class TokenResponseSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()

class JWTSerializer(BaseJWTSerializer):
    """
    Serializer for JWT authentication.
    """
    token = TokenResponseSerializer(required=True)
