from django.shortcuts import render


def dashboard(request):
    return render(request, 'portal/dashboard.html')


def products(request):
    return render(request, 'portal/products.html')


def customers(request):
    return render(request, 'portal/customers.html')
