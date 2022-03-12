from django.shortcuts import render
from django.http import HttpResponse


from .models import *

from collections import defaultdict

def index(request):

    invoices = Invoice.objects.all()
    
    
    for invoice in invoices:
        products = InvoiceItem.objects.filter(invoice=invoice.id)
        invoice_items = defaultdict(lambda:0,{})
        
        total_price = 0
        for product in products:
            invoice_items[product.product.name] = product.quantity
            total_price += product.quantity * product.unit_price


    """
    SAKURA = 'Sakura'
    ROMANCE = 'Romance'
    JUICY = 'Juicy'
    INTRICATE = 'Intricate'
    DESTINY = 'Destiny'
    HONEY = 'Honey'
    PL = 'Pl'
    FLORAL = 'Floral'
    """        

  

    order = {
        'invoices' : invoices,
        'products' : products 
    }



    return render(request, 'invoice/index.html', order)

def create_invoice(request):

   
    return render(request, 'invoice/invoice.html')



# Create your views here.
