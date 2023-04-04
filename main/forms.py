from django.forms import ModelForm
from .models import AirportTaxiService, AccommodationService


class AirportTaxiServiceForm(ModelForm):
    class Meta:
        model = AirportTaxiService
        fields = ['car_type', 'address', 'journey_type', 'travel_date', 'travel_time']


class AccommodationServiceForm(ModelForm):
    class Meta:
        model = AccommodationService
        fields = ['accommodation_type', 'occupancy', 'address', 'move_in_date']