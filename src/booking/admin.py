from django.contrib import admin
from .models import User, Space, Reservation

admin.site.register(User)
admin.site.register(Space)
admin.site.register(Reservation)