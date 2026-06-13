from django.contrib import admin

from .models import Reservation, Space, SpaceOwner

admin.site.register(Space)
admin.site.register(Reservation)
admin.site.register(SpaceOwner)
