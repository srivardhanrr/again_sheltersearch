from django.db import models
from django.contrib.auth.models import User


class AirportTaxiService(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    journey_type = models.CharField(max_length=40)
    car_type = models.CharField(max_length=10, default="sedan")
    travel_date = models.DateField()
    travel_time = models.TimeField()
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Regret', 'Regret'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    address = models.CharField(max_length=200)
    order_id = models.CharField(max_length=50, unique=True)
    checked = models.CharField(max_length=5, blank=True, choices=(("Y", "Yes"), ("N", "No")))
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class AccommodationService(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    accommodation_type = models.CharField(max_length=20)
    occupancy = models.CharField(max_length=15)
    move_in_date = models.DateField()
    gender = models.CharField(max_length=7, null=True, blank=True)
    address = models.CharField(max_length=200)
    order_id = models.CharField(max_length=50, unique=True)
    checked = models.CharField(max_length=5, blank=True, choices=(("Y", "Yes"), ("N", "No")))
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class HotelService(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.CharField(max_length=20)
    room = models.CharField(max_length=15)
    people = models.CharField(max_length=15)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    address = models.CharField(max_length=200)
    order_id = models.CharField(max_length=50, unique=True)
    date = models.CharField(default="Yes", max_length=23)
    checked = models.CharField(max_length=5, blank=True, choices=(("Y", "Yes"), ("N", "No")))
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)