from django.contrib import admin
from .models import *


@admin.register(AirportTaxiService)
class AirportTaxiServiceAdmin(admin.ModelAdmin):
    list_display = ("client", "created_at", "journey_type", "status", )
    list_editable = ("status", )


@admin.register(AccommodationService)
class AirportTaxiServiceAdmin(admin.ModelAdmin):
    list_display = ("client", "created_at", "accommodation_type", "occupancy", )
