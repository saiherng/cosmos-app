from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from .models import *
from .forms import *

from collections import defaultdict


def orders(request):
    invoices = Invoice.objects.all()
    data = []
    products = {}

    for invoice in invoices:
        # contains all items in an invoice
        cart = InvoiceItem.objects.filter(invoice=invoice.id)

        invoice_items = {
            "Sakura": 0,
            "Romance": 0,
            "Juicy": 0,
            "Intricate": 0,
            "Destiny": 0,
            "Honey": 0,
            "Pl": 0,
            "Floral": 0,
            "Total": 0
        }

        total_price = 0
        for product in cart:
            invoice_items[product.product.name] = product.quantity
            total_price += product.quantity * product.unit_price

        invoice_items["Total"] = str(total_price) + " ks"
        products[invoice.id] = invoice_items

        data.append([invoice, invoice_items])

        invoice_items = {
            "Sakura": 0,
            "Romance": 0,
            "Juicy": 0,
            "Intricate": 0,
            "Destiny": 0,
            "Honey": 0,
            "Pl": 0,
            "Floral": 0,
            "Total": 0
        }

    product_sales = {}
    order = {
        'invoices': data,
        'product_sales': product_sales
    }

    return render(request, 'invoice/index.html', order)


def create_invoice(request):

    return render(request, 'invoice/invoice.html')


def create_customer(request):

    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            f_name = form.cleaned_data['f_name']
            f_phone_number = form.cleaned_data['f_phone_number']
            f_email = form.cleaned_data['f_email']
            f_address = form.cleaned_data['f_address']

            print(f_name)
            customer = Customer(name=f_name, phone_number=f_phone_number,
                                email=f_email, address=f_address)
            customer.save()

            return HttpResponse("Success")

    return render(request, 'invoice/invoice.html', {'form': form})


def display_products(request):

    products = Product.objects.all()
    context = {
        "products": products
    }

    return render(request, 'invoice/products.html', context)

# Create your views here.
