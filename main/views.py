from django.views.generic import TemplateView
from .forms import AirportTaxiServiceForm, AccommodationServiceForm, HotelServiceForm
from .models import AirportTaxiService, AccommodationService, HotelService
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from django.utils import timezone


class IndexPageView(TemplateView):
    template_name = 'main/dashboard.html'

    def get(self, request, **kwargs):
        taxi = AirportTaxiService.objects.filter(client=self.request.user)
        hotel = HotelService.objects.filter(client=self.request.user)
        accommodation = AccommodationService.objects.filter(client=self.request.user)

        context = {
            'airport_services': taxi,
            'accommodation_services': accommodation,
            'hotel_services': hotel
        }
        return render(request, self.template_name, context)


class IndexPageViewM(TemplateView):
    template_name = 'main/dashboard_m.html'

    def get(self, request, **kwargs):
        taxi = AirportTaxiService.objects.filter(client=self.request.user)
        hotel = HotelService.objects.filter(client=self.request.user)
        accommodation = AccommodationService.objects.filter(client=self.request.user)

        context = {
            'airport_services': taxi,
            'accommodation_services': accommodation,
            'hotel_services': hotel
        }
        return render(request, self.template_name, context)


class HotelServiceViewM(TemplateView):
    template_name = 'main/hotel_service_m.html'
    form_class = HotelServiceForm

    def post(self, request):
        form = self.form_class(request.POST)
        if not form.is_valid():
            print("Not Valid")
            messages.error(request, "Form Invalid.")
            return render(request, self.template_name)
        booking = form.save(commit=False)
        if HotelService.objects.filter(order_id=request.POST.get('order_id')).exists():
            messages.error(request, "Order id already exists. Please refresh the page and try again.")
            return redirect("main:hotel_m")
        now = timezone.now()
        booking.order_id = f'{now.year}{now.month}{now.day}-{uuid.uuid4().hex}'
        booking.client = self.request.user
        booking.save()
        messages.success(request, "Your request for Hotel Booking has been placed successfully. You will receive a confirmation email shortly.")
        return redirect("main:hotel_m")


class HotelServiceView(TemplateView):
    template_name = 'main/hotel_service.html'
    form_class = HotelServiceForm

    def post(self, request):
        form = self.form_class(request.POST)
        if not form.is_valid():
            print("Not Valid")
            messages.error(request, "Form Invalid.")
            return render(request, self.template_name)
        booking = form.save(commit=False)
        if HotelService.objects.filter(order_id=request.POST.get('order_id')).exists():
            messages.error(request, "Order id already exists. Please refresh the page and try again.")
            return redirect("main:hotel")
        now = timezone.now()
        booking.order_id = f'{now.year}{now.month}{now.day}-{uuid.uuid4().hex}'
        booking.client = self.request.user
        booking.save()
        messages.success(request, "Your request for Hotel Booking has been placed successfully. You will receive a confirmation email shortly.")
        return redirect("main:hotel")


class TaxiServiceViewM(TemplateView):
    template_name = 'main/taxi_service_m.html'
    form_class = AirportTaxiServiceForm

    def post(self, request):
        form = self.form_class(request.POST)
        if not form.is_valid():
            print("Not Valid")
            messages.error(request, "Form Invalid.")
            return render(request, self.template_name)
        booking = form.save(commit=False)
        if AirportTaxiService.objects.filter(order_id=request.POST.get('order_id')).exists():
            messages.error(request, "Order id already exists. Please refresh the page and try again.")
            return redirect("main:taxi_m")
        now = timezone.now()
        booking.order_id = f'{now.year}{now.month}{now.day}-{uuid.uuid4().hex}'
        booking.client = self.request.user
        booking.save()
        messages.success(request, "Your request for Airport taxi has been placed successfully. You will receive a confirmation email shortly.")
        return redirect("main:taxi_m")


class TaxiServiceView(TemplateView):
    template_name = 'main/taxi_service.html'
    form_class = AirportTaxiServiceForm

    def post(self, request):
        form = self.form_class(request.POST)
        if not form.is_valid():
            print("Not Valid")
            messages.error(request, "Form Invalid.")
            return render(request, self.template_name)
        booking = form.save(commit=False)
        if AirportTaxiService.objects.filter(order_id=request.POST.get('order_id')).exists():
            messages.error(request, "Order id already exists. Please refresh the page and try again.")
            return redirect("main:taxi")
        now = timezone.now()
        booking.order_id = f'{now.year}{now.month}{now.day}-{uuid.uuid4().hex}'
        booking.client = self.request.user
        booking.save()
        messages.success(request, "Your request for Airport taxi has been placed successfully. You will receive a confirmation email shortly.")
        return redirect("main:taxi")


class AccommodationServiceViewM(TemplateView):
    template_name = 'main/accom_service_m.html'
    form_class = AccommodationServiceForm

    def post(self, request):
        form = self.form_class(request.POST)
        if not form.is_valid():
            print(form.errors)
            messages.error(request, "Form is Invalid.")
            return redirect("main:accommodation_m")
        booking = form.save(commit=False)
        if AccommodationService.objects.filter(order_id=request.POST.get('order_id', )).exists():
            messages.error(request, "Order id already exists. Please refresh the page and try again.")
            return redirect("main:accommodation")
        if request.POST.get("accommodation_type") == "Pg":
            booking.gender = request.POST.get("gender")
        now = timezone.now()
        booking.order_id = f'{now.year}{now.month}{now.day}-{uuid.uuid4().hex}'
        booking.client = self.request.user
        booking.save()
        messages.success(request,
                         "Your request for Accommodation has been placed successfully. You will receive a confirmation email shortly.")
        return redirect("main:accommodation_m")


class AccommodationServiceView(TemplateView):
    template_name = 'main/accom_service.html'
    form_class = AccommodationServiceForm

    def post(self, request):
        form = self.form_class(request.POST)
        if not form.is_valid():
            print(form.errors)
            messages.error(request, "Form is Invalid.")
            return redirect("main:accommodation")
        booking = form.save(commit=False)
        if AccommodationService.objects.filter(order_id=request.POST.get('order_id', )).exists():
            messages.error(request, "Order id already exists. Please refresh the page and try again.")
            return redirect("main:accommodation")
        if request.POST.get("accommodation_type") == "Pg":
            booking.gender = request.POST.get("gender")
        now = timezone.now()
        booking.order_id = f'{now.year}{now.month}{now.day}-{uuid.uuid4().hex}'
        booking.client = self.request.user
        booking.save()
        messages.success(request,
                         "Your request for Accommodation has been placed successfully. You will receive a confirmation email shortly.")
        return redirect("main:accommodation")


class TestPageView(TemplateView):
    template_name = 'main/test.html'


class HotelBookingView(TemplateView):
    template_name = 'main/hotel_booking.html'

    def get(self, request, order_id):
        service = get_object_or_404(HotelService, order_id=order_id)
        return render(request, self.template_name, {'service': service})



