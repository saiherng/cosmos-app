from django.urls import path

from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('create-invoice/', views.create_invoice, name='invoice'),
    path('products/', views.display_products, name='products'),
    path('create-customer/', views.create_customer, name='form_customer'),
]
