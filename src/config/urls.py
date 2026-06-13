from django.contrib import admin
from django.urls import path

from booking.views import (
    ReservationCreateAPIView,
    ReservationDestroyAPIView,
    SpaceCreateAPIView,
    SpaceDestroyAPIView,
    SpaceListAPIView,
    SpaceOwnerListAPIView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # Пространства
    path("spaces/", SpaceListAPIView.as_view()),
    path("spaces/create/", SpaceCreateAPIView.as_view()),
    path("spaces/<int:pk>/delete/", SpaceDestroyAPIView.as_view()),
    # Владельцы пространств
    path("owners/<int:pk>/spaces/", SpaceOwnerListAPIView.as_view()),
    # Бронирования
    path("reservations/create/", ReservationCreateAPIView.as_view()),
    path("reservations/<int:pk>/delete/", ReservationDestroyAPIView.as_view()),
]
