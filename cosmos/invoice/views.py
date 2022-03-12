from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def index(request):

    invoice = Invoice.objects.get(pk=1)
    customer = invoice.customer
    

    context = {
        'invoice' : invoice,
        'customer': customer
        
       
    }

    return render(request, 'invoice/index.html', context)

def create_invoice(request):

   
    return render(request, 'invoice/invoice.html')



# Create your views here.
