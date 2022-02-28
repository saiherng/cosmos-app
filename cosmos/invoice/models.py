from email.policy import default
from django.db import models
from django.forms import DateField
from django.utils import timezone


class Customer(models.Model):

    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)

    @property
    def getName(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)


class Invoice(models.Model):

    KPAY = "K"
    CASH = "C"

    PAYMENT_TYPE = [
        (KPAY, 'KP'),
        (CASH, 'Cash'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    date = DateField()
    items = models.ManyToManyField(
        'Product',
        related_name='carts')

    payment = models.CharField(max_length=1, choices=PAYMENT_TYPE)
    payment_id = models.CharField(max_length=20, default='cash')

    @property
    def __str__(self):
        return self.customer


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
    #description = models.CharField(max_length=200, default='', null=True, blank=True)

    @property
    def getName(self):
        return str(self.name)

    def __str__(self):
        return self.name
