from django.contrib import admin

from .models import Reservation, Space, User

admin.site.register(User)
admin.site.register(Space)
admin.site.register(Reservation)
