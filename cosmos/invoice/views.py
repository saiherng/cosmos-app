from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'invoice/index.html')

def create_invoice(request):
    return render(request, 'invoice/invoice.html')

# Create your views here.
