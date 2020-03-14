from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import (
    logout as django_logout
)
from django.utils.translation import ugettext_lazy as _

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, SlidingToken, UntypedToken
from rest_auth.app_settings import create_token
from rest_auth.views import (
    LoginView as BaseLogin,
    LogoutView as BaseLogout)
from drf_yasg.utils import swagger_auto_schema



class LoginView(BaseLogin):
    """
    """
    def login(self):
        self.user = self.serializer.validated_data['user']

        if getattr(settings, 'REST_USE_JWT', False):
            self.token = RefreshToken.for_user(self.user)
        else:
            self.token = create_token(self.token_model, self.user,
                                      self.serializer)

        if getattr(settings, 'REST_SESSION_LOGIN', True):
            self.process_login()

    def get_response(self):
        serializer_class = self.get_response_serializer()

        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': self.user,
                'token': {
                    'access': str(self.token.access_token),
                    'refresh': str(self.token)
                }
            }
            serializer = serializer_class(instance=data,
                                          context={'request': self.request})
        else:
            serializer = serializer_class(instance=self.token,
                                          context={'request': self.request})

        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response



class LogoutView(BaseLogout):
    permission_classes = (IsAuthenticated,)
    
    @swagger_auto_schema(auto_schema=None)
    def get(self, request, *args, **kwargs):
        return super().get()

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        if getattr(settings, 'REST_SESSION_LOGIN', True):
            django_logout(request)

        response = Response({"detail": _("Successfully logged out.")},
                            status=status.HTTP_200_OK)
        if getattr(settings, 'REST_USE_JWT', False):
            token = RefreshToken(None)
            token.blacklist()
            if settings.JWT_AUTH_COOKIE:
                response.delete_cookie(settings.JWT_AUTH_COOKIE)
        return response
