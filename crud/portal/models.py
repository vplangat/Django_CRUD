from django.db import models

BASE_UNIT = (
    ('packet', 'PACKET'),
    ('cartoon', 'CARTOON'),
    ('gallons', 'GALLONS'),
    ('pounds', 'POUNDS'),
    ('tons', 'TONS'),
    ('kilograms', 'KILOGRAMS'),
    ('gram', 'GRAM'),
    ('liters', 'LITERS'),
    ('each', 'EACH')
)


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=255, null=True)
    unit_price = models.FloatField(max_length=50, null=True)
    base_price = models.FloatField(max_length=50, null=True)
    base_unit = models.CharField(max_length=20, choices=BASE_UNIT, default="packet", null=True)
    quantity = models.IntegerField(max_length=10, null=True)
    is_in_stock = models.BooleanField(default=True)
    is_limited = models.BooleanField(default=True)
