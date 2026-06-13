from django.utils import timezone
from rest_framework import serializers

from .models import Reservation, Space


class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

    def validate(self, attrs):
        start_time = attrs.get("start_time")
        end_time = attrs.get("end_time")
        space = attrs.get("space")

        if start_time < timezone.localdate():
            raise serializers.ValidationError(
                "Дата начала не может быть раньше сегодняшней."
            )

        if start_time > end_time:
            raise serializers.ValidationError(
                "Дата начала должна быть раньше или равно дате окончания."
            )

        conflict = Reservation.objects.filter(
            space=space,
            start_time__lt=end_time,
            end_time__gt=start_time,
        )

        if conflict.exists():
            raise serializers.ValidationError(
                "Этот номер уже забронирован на выбранные даты."
            )

        return attrs
