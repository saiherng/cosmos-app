from email.policy import default
from django.db import models
from django.forms import DateField
from django.utils import timezone


class Customer(models.Model):

    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField(default="")
    address = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):

    SAKURA = 'SK'
    ROMANCE = 'RM'
    JUICY = 'JY'
    INTRICATE = 'IE'
    DESTINY = 'DY'
    HONEY = 'HY'
    PL = 'PL'
    FLORAL = 'FL'

    PRODUCT = [
        (SAKURA, 'Sakura'),
        (ROMANCE, 'Romance'),
        (JUICY, 'Juicy'),
        (INTRICATE, 'Intricate'),
        (DESTINY, 'Destiny'),
        (HONEY, 'Honey'),
        (PL, 'Pl'),
        (FLORAL, 'Floral'),
    ]

    name = models.CharField(max_length=2, choices=PRODUCT)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    #invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    #description = models.CharField(max_length=200, default='', null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Invoice(models.Model):

    KPAY = "K"
    CASH = "C"

    PAYMENT_TYPE = [
        (KPAY, 'KP'),
        (CASH, 'Cash'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    date = DateField()
    items = models.ManyToManyField(Product)

    payment = models.CharField(max_length=1, choices=PAYMENT_TYPE)
    payment_id = models.CharField(max_length=20, default='cash')


    class Meta:
        ordering = ['customer']

    def __str__(self):
        return self.customer.name