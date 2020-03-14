from django.urls import path, re_path, include
from rest_framework import routers

app_name = "users"

routers = routers.DefaultRouter()

urlpatterns = [
    path("", include(routers.urls)),
]
