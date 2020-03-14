from django.urls import path, re_path, include

from rest_auth.registration.views import VerifyEmailView, RegisterView
from rest_auth.views import (
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from django.conf import settings
from auth.views import LoginView, LogoutView

rest_auth_registration_urls = [
    # allauth login/logout/password
    re_path(r"^registration/$", RegisterView.as_view(), name="account_signup"),
    re_path(r"^registration/verify-email/$",VerifyEmailView.as_view(),name="rest_verify_email",)
]


urlpatterns = [
    # rest_auth login/logout/password
    re_path(r"^login/$", LoginView.as_view(), name="rest_login"),
    re_path(r"^logout/$", LogoutView.as_view(), name="rest_logout"),
    re_path(r"^password/reset/$", PasswordResetView.as_view(), name="rest_password_reset"),
    re_path(r"^password/reset/confirm/$",PasswordResetConfirmView.as_view(),name="rest_password_reset_confirm",),
    re_path(r"^password/change/$", PasswordChangeView.as_view(), name="rest_password_change" ),

    #rest_framework_simplejwt
    re_path(r"^token/obtain/$", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r"^token/refresh/$", TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r"^token/verify/$", TokenVerifyView.as_view(), name='token_verify'),

]

if settings.AUTH_ALLOW_REGISTRATION:
    urlpatterns += rest_auth_registration_urls
