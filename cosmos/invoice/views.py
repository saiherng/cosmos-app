from django.shortcuts import render
from django.http import HttpResponse


from .models import *

from collections import defaultdict

def index(request):

    invoices = Invoice.objects.all()
    data = []
    products = {}
    
    for invoice in invoices:
        
        
        #contains all items in an invoice
        cart = InvoiceItem.objects.filter(invoice=invoice.id)
        
        invoice_items = {
            "Sakura" : 0,
            "Romance" : 0,
            "Juicy" : 0,
            "Intricate" : 0,
            "Destiny" : 0,
            "Honey" : 0,
            "Pl" : 0,
            "Floral" : 0,
            "Total" : 0
        }

        total_price = 0
        for product in cart:
            invoice_items[product.product.name] = product.quantity
            total_price += product.quantity * product.unit_price
        
        invoice_items["Total"] = str(total_price) + " ks"
        products[invoice.id] = invoice_items

        data.append([invoice, invoice_items])
    
    order = {
        'invoices' : data,
    }

    return render(request, 'invoice/index.html', order)

def create_invoice(request):

    
    return render(request, 'invoice/invoice.html')


def display_products(request):

    products = Product.objects.all()

    context = {
        "products" : products
    }

    return render(request, 'invoice/products.html', context)

# Create your views here.
