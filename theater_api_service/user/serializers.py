from rest_framework import serializers

from theater_api_service.user.models import User


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = "__all__"
