from loguru import logger
from rest_framework import filters
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView

from .models import Reservation, Space
from .serializers import ReservationSerializer, SpaceSerializer


class SpaceCreateAPIView(CreateAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer

    def perform_create(self, serializer):
        space = serializer.save()

        logger.info("Создано пространство", extra={"space_id": space.id})


class SpaceDestroyAPIView(DestroyAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer

    def perform_destroy(self, instance):
        logger.warning("Удаление пространства", extra={"space_id": instance.id})
        return super().perform_destroy(instance)


class SpaceOwnerListAPIView(ListAPIView):
    serializer_class = SpaceSerializer

    def get_queryset(self):
        owner_id = self.kwargs["pk"]

        logger.info("Запрос списка пространств владельца", extra={"owner_id": owner_id})

        return Space.objects.filter(owner_id=owner_id)


class ReservationCreateAPIView(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        reservation = serializer.save()

        logger.info(
            "Создано бронирование",
            extra={
                "reservation_id": reservation.id,
                "space_id": reservation.space_id,
                "user_id": getattr(self.request.user, "id", None),
            },
        )


class ReservationDestroyAPIView(DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_destroy(self, instance):
        logger.warning(
            "Удаление бронирования",
            extra={
                "reservation_id": instance.id,
                "space_id": instance.space_id,
            },
        )
        return super().perform_destroy(instance)


class SpaceListAPIView(ListAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["price"]
    ordering = ["price"]

    def list(self, request, *args, **kwargs):
        logger.info(
            "Получение списка пространств",
            extra={
                "user_id": getattr(request.user, "id", None),
                "ordering": request.query_params.get("ordering"),
            },
        )
        return super().list(request, *args, **kwargs)
