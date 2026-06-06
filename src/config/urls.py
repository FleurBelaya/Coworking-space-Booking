from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from booking.views import SpaceAPI, UserAPI, ReservationAPI

router = routers.SimpleRouter()
router.register(r'users', UserAPI )
router.register(r'reservations', ReservationAPI)
router.register(r'spaces', SpaceAPI)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
