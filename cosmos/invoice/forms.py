from django import forms


class CustomerForm(forms.Form):
    f_name = forms.CharField(label='Your name', max_length=100)
    f_phone_number = forms.IntegerField(label='Your phone')
    f_email = forms.EmailField(label='Your email')
    f_address = forms.CharField(label='Your address', max_length=100)
