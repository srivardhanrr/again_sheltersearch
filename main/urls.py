from django.urls import path
from main.views import *


urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('m/', IndexPageViewM.as_view(), name='index_m'),

    path('taxi/', TaxiServiceView.as_view(), name='taxi'),
    path('taxi/m/', TaxiServiceViewM.as_view(), name='taxi_m'),

    path('accommodation/', AccommodationServiceView.as_view(), name='accommodation'),
    path('accommodation/m/', AccommodationServiceViewM.as_view(), name='accommodation_m'),

    path('hotel/', HotelServiceView.as_view(), name='hotel'),
    path('hotel/m/', HotelServiceViewM.as_view(), name='hotel_m'),
    path('hotel/<order_id>', HotelBookingView.as_view(), name='hotel_b'),

    path('test/', TestPageView.as_view(), name='test'),
]