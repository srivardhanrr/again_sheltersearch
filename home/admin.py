from django.contrib import admin
from .models import *


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("name", "address")


@admin.register(PayingGuest)
class PayingGuestAdmin(admin.ModelAdmin):
    list_display = ("name", "college", "distance",)
    list_filter = ("college",)


@admin.register(Contacts)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "gender", "created_at", "checked")
    list_editable = ("checked", )


@admin.register(Partners)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Testimonials)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ServiceInfo)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("happy_clients",)



