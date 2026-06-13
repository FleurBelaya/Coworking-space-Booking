from django.utils import timezone
from loguru import logger
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

        logger.debug(
            "Начата валидация бронирования",
            extra={
                "space_id": getattr(space, "id", None),
                "start_time": str(start_time),
                "end_time": str(end_time),
            },
        )

        if start_time < timezone.localdate():
            logger.warning(
                "Отклонено бронирование: дата начала раньше сегодняшней",
                extra={"start_time": str(start_time)},
            )
            raise serializers.ValidationError(
                "Дата начала не может быть раньше сегодняшней."
            )

        if start_time > end_time:
            logger.warning(
                "Отклонено бронирование: некорректный диапазон дат",
                extra={
                    "start_time": str(start_time),
                    "end_time": str(end_time),
                },
            )
            raise serializers.ValidationError(
                "Дата начала должна быть раньше или равна дате окончания."
            )

        conflict = Reservation.objects.filter(
            space=space,
            start_time__lt=end_time,
            end_time__gt=start_time,
        )

        if conflict.exists():
            logger.warning(
                "Отклонено бронирование: найден конфликт по датам",
                extra={
                    "space_id": space.id,
                    "start_time": str(start_time),
                    "end_time": str(end_time),
                },
            )
            raise serializers.ValidationError(
                "Это пространство уже забронировано на выбранные даты."
            )

        logger.info(
            "Бронирование прошло валидацию успешно",
            extra={
                "space_id": space.id,
                "start_time": str(start_time),
                "end_time": str(end_time),
            },
        )

        return attrs
