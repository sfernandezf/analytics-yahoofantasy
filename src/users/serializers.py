from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "created_timestamp",
            "updated_timestamp",
            "email",
            "first_name",
            "last_name",
        )
