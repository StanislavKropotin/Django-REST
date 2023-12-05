from rest_framework import serializers

from .models import*

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("__all__")


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("__all__")


# class UserSerializer(serializers.py.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ("__all__")        