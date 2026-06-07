from django.contrib import admin
from django.urls import path

from booking.views import SpaceOwnerListAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("owners/<int:owner_id>/spaces/", SpaceOwnerListAPIView.as_view()),
]
