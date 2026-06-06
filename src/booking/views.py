from rest_framework import viewsets
from .models import User, Space, Reservation
from .serializers import (
    UserSerializer,
    SpaceSerializer,
    ReservationSerializer,
)


class SpaceAPI(viewsets.ModelViewSet):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer


class UserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReservationAPI(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer