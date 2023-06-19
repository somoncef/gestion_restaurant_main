from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display=["user","date"]

admin.site.register(Reservation,ReservationAdmin)   
