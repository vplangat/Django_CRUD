from django.shortcuts import render
from .models import *


def dashboard(request):
    total_customers = Customer.objects.all()
    total_products = Product.objects.all()
    total_orders = Order.objects.all()
    context = {'customers': total_customers, 'products': total_products, 'orders': total_orders}
    return render(request, 'portal/dashboard.html', context)


def products(request):
    total_products = Product.objects.all()
    return render(request, 'portal/products.html', {'products': total_products})


def customers(request):
    return render(request, 'portal/customers.html')
