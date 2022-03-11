
from django.db import models


class Customer(models.Model):

    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)

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
    description = models.CharField(
        max_length=200, default='', null=True, blank=True)

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
    placed_at = models.DateTimeField(auto_now_add=True)

    payment = models.CharField(
        max_length=1, choices=PAYMENT_TYPE, default=CASH)
    payment_account = models.CharField(max_length=20, default='cash')

    def __str__(self):
        return self.customer


class InvoiceItem(models.Model):

    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.IntegerField()


class Cart(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
