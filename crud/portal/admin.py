from django.contrib import admin
from .models import *  # Customer, Product, Vendors, Order

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Vendor)
admin.site.register(Order)
admin.site.register(Tag)
