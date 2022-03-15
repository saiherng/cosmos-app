from django import forms
from django.forms import ModelForm
from .models import *


class CustomerForm(ModelForm):
    # f_name = forms.CharField(label='Your name', max_length=100)
    # f_phone_number = forms.IntegerField(label='Your phone')
    # f_email = forms.EmailField(label='Your email')
    # f_address = forms.CharField(label='Your address', max_length=100)

    class Meta:
        model = Customer
        fields = "__all__"


class InvoiceForm(ModelForm):
    # f_name = forms.CharField(label='Your name', max_length=100)
    # f_phone_number = forms.IntegerField(label='Your phone')
    # f_email = forms.EmailField(label='Your email')
    # f_address = forms.CharField(label='Your address', max_length=100)

    class Meta:
        model = Invoice
        fields = "__all__"
