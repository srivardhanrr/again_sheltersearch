from django.forms import ModelForm
from .models import Contacts, Register


class ContactForm(ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
