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

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Electronic', 'ELECTRONIC'),
        ('Footwear', 'FOOTWEAR'),
        ('Consumable', 'CONSUMABLE'),
        ('Clothing', 'CLOTHING'),
        ('Industrial', 'INDUSTRIAL')
    )
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    unit_price = models.FloatField(null=True)
    base_price = models.FloatField(null=True)
    base_unit = models.CharField(max_length=20, choices=BASE_UNIT, default="packet", null=True)
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    quantity = models.IntegerField(null=True)
    is_in_stock = models.BooleanField(default=True)
    is_limited = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'PENDING'),
        ('Out of Stock', 'OUT_OF_STOCK'),
        ('Delivered', 'DELIVERED'),
        ('Shipment', 'SHIPMENT')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices=STATUS, default="Pending", null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

 
class Vendor(models.Model):
    name = models.CharField(max_length=200, null=True)
    telephone = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=200, null=True)
    product_lines = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
