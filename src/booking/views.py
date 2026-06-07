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
        company_name = self.kwargs["company_name"]
        return Space.objects.filter(spaceowner__company_name=company_name)


class ReservationCreateAPIView(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationDestroyAPIView(DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationListAPIView(ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
