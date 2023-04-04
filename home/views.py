import asyncio
import threading
import time
import random
import hashlib
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.template.loader import render_to_string
from django.views import View
from asgiref.sync import sync_to_async
from .models import *
from .forms import ContactForm, RegisterForm
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


# import razorpay
# from .keys import RAZORPAY_ID, RAZORPAY_SECRET


class HomeView(View):
    template_name = "home/home.html"

    async def get(self, request):
        partners = asyncio.ensure_future(self.get_partners())
        testimonials = asyncio.ensure_future(self.get_testimonials())
        await asyncio.wait([partners, testimonials])
        context = {'partners': partners, 'testimonials': testimonials}
        return render(request, "home/home.html", context)

    @sync_to_async
    def get_partners(self):
        return Partners.objects.all()

    @sync_to_async
    def get_testimonials(self):
        testimonials = Testimonials.objects.all()
        for t in testimonials:
            z = []
            z.extend(iter(range(1, t.rating + 1)))
            t.rating = z
        return testimonials


class ContactView(View):
    template_name = "home/contact.html"
    form_class = ContactForm

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name)
        form.save()
        email_subject = f'New contact: {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
        email_message = f'Name: {form.cleaned_data["name"]} \nMessage: {form.cleaned_data["message"]}'
        EmailThread(email_subject, email_message, ["srivardhan.singh.rathore@gmail.com"]).start()
        return HttpResponse(status=200)


class RegisterView(View):
    template_name = "home/register.html"
    form_class = RegisterForm

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            try:
                email_subject = f'Registration Successful {form.cleaned_data["email"]}: {form.cleaned_data["name"]}'
                context = {"name": form.cleaned_data["name"],
                           "email": form.cleaned_data["email"],
                           "phone": form.cleaned_data["phone"]}

                message = render_to_string("home/email_template/signup_success.html", context=context)
                EmailThread(email_subject, message, [f'{form.cleaned_data["email"]}']).start()
                EmailThread(email_subject, "New Contact", ['srivardhan.singh.rathore@gmail.com']).start()
            except Exception:
                messages.error(request, f"Error occured: {Exception}.")
                print(Exception)
                redirect("/")
            return redirect("/")


def logout_user(request):
    logout(request)
    return redirect("accounts:log_in")


def dashboard(request):
    user = request.user
    return render(request, "home/dashboard.html", {"user": user})


class PolicyView(View):
    template_dir = "home/policies/"

    def get(self, request, called):
        if called == "terms_of_service":
            return render(request, f"{self.template_dir}terms_of_service.html")
        elif called == "privacy_policy":
            return render(request, f"{self.template_dir}privacy_policy.html")
        elif called == "refund_policy":
            return render(request, f"{self.template_dir}refund_policy.html")
        else:
            return render(request, "home/404.html")


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list, html_message=None):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        self.html_message = html_message
        threading.Thread.__init__(self)

    def run(self):
        message = EmailMessage(self.subject, self.html_content, settings.CONTACT_EMAIL,
                               self.recipient_list)
        message.content_subtype = "html"
        message.send(fail_silently=False)
        print(message.to)


def email_verification(email):
    start = time.time()
    otp = random.randrange(100000, 999999)
    email_subject = "Email Verification code - Sheltersearch"
    message = f"The otp to verify your Email Address is {otp}."
    EmailThread(email_subject, message, [email]).start()
    hash_value = hashlib.sha256(string=str(otp).encode())
    print(time.time() - start)
    return hash_value.hexdigest()
