from django.urls import path
from main.views import IndexPageView, TaxiServiceView, AccommodationServiceView, HotelServiceView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('taxi/', TaxiServiceView.as_view(), name='taxi'),
    path('accommodation/', AccommodationServiceView.as_view(), name='accommodation'),
    path('hotel/', HotelServiceView.as_view(), name='hotel')
]