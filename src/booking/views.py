from rest_framework import filters
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView

from .models import Reservation, Space
from .serializers import (
    ReservationSerializer,
    SpaceSerializer,
)


class SpaceCreateAPIView(CreateAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer


class SpaceDestroyAPIView(DestroyAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer


class SpaceOwnerListAPIView(ListAPIView):
    serializer_class = SpaceSerializer

    def get_queryset(self):
        owner_id = self.kwargs["pk"]
        return Space.objects.filter(owner_id=owner_id)


class ReservationCreateAPIView(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationDestroyAPIView(DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class SpaceListAPIView(ListAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["price"]
    ordering = ["price"]
