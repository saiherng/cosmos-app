from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-invoice/', views.create_invoice, name='invoice'),
    path('products/', views.display_products, name='products')
]
