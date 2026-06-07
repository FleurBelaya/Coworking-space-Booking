from rest_framework import serializers

from .models import Reservation, Space, User


class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
