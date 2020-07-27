"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic.base import RedirectView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.urls import get_resolver, get_urlconf

from leagues.views import LeagueViews
from results.views import ResultViews
from teams.views import TeamViews


schema_view = get_schema_view(
    openapi.Info(
        title="Yahoo Fantasy Analytics",
        default_version="v1",
        description="Yahoo Fantasy Analytics",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sfernandezf90@gmail.com"),
        # license=openapi.License(name="BSD License"),
    ),
    permission_classes=(permissions.AllowAny,),
    public=True
)


urlpatterns = [
    # admin
    re_path(r"^admin/", admin.site.urls),
    # # api
    # swagger
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    # auth
    re_path(r"^api/auth/", include("auth.urls")),
    # users
    re_path(r"^api/users/", include(("users.urls", "users"), namespace="users")),
    re_path(r"^standings/", LeagueViews.as_view()),
    re_path(r"^matchups/", ResultViews.as_view()),
    re_path(r"^stats/", TeamViews.as_view()),
    re_path(r'^.*$', RedirectView.as_view(url='/standings/', permanent=False), name='index')


]
