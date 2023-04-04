from django.views.generic import TemplateView
from .forms import AirportTaxiServiceForm, AccommodationServiceForm
from .models import AirportTaxiService, AccommodationService
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from django.utils import timezone


class IndexPageView(TemplateView):
    template_name = 'main/dashboard.html'


class HotelServiceView(TemplateView):
    template_name = 'main/hotel_service.html'


class TaxiServiceView(TemplateView):
    template_name = 'main/taxi_service.html'
    form_class = AirportTaxiServiceForm

    def get(self, request, **kwargs):
        now = timezone.now()
        order_id = f'{now.year}{now.month}{now.day}-{uuid.uuid4().hex}'
        context = {'order_id': order_id}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if not form.is_valid():
            print("Not Valid")
            messages.error(request, "Form Invalid.")
            return render(request, self.template_name)
        booking = form.save(commit=False)
        if AirportTaxiService.objects.filter(order_id=request.POST.get('order_id', )).exists():
            messages.error(request, "Order id already exists. Please refresh the page and try again.")
            return redirect("main:taxi")
        booking.order_id = request.POST.get('order_id', )
        booking.client = self.request.user
        booking.save()
        messages.success(request, "Your request for Airport taxi has been placed successfully. You will receive a confirmation email shortly.")
        return redirect("main:taxi")


class AccommodationServiceView(TemplateView):
    template_name = 'main/accom_service.html'
    form_class = AccommodationServiceForm

    def get(self, request, **kwargs):
        now = timezone.now()
        order_id = f'{now.year}{now.month}{now.day}-{uuid.uuid4().hex}'
        context = {'order_id': order_id}
        return render(request, self.template_name, context)

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
        booking.order_id = request.POST.get('order_id')
        booking.client = self.request.user
        booking.save()
        messages.success(request,
                         "Your request for Accommodation has been placed successfully. You will receive a confirmation email shortly.")
        return redirect("main:accommodation")



