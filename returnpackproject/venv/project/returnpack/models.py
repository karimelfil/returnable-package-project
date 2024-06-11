from django.db import models

# Create your models here.
from django.db import models



# Create your models here.

class Customer(models.Model):
    type=models.CharField(max_length=100,default="default value")
    firstname=models.CharField(max_length=100,default="default value")
    lastname=models.CharField(max_length=100,default="default value")
    email=models.CharField(max_length=100,default="default value")
    website=models.CharField(max_length=100,default="default value")
    workphone=models.IntegerField()
    phone=models.IntegerField()
    contact=models.CharField(max_length=100,default="default value")

class Supplier(models.Model):
    type=models.CharField(max_length=100,default="default value")
    firstname=models.CharField(max_length=100,default="default value")
    lastname=models.CharField(max_length=100,default="default value")
    email=models.CharField(max_length=100,default="default value")
    workphone=models.IntegerField()
    phone=models.IntegerField()

class Category(models.Model):
    name=models.CharField(max_length=100,default="default value")
    description=models.CharField(max_length=100,default="default value")


class Item(models.Model):
    name = models.CharField(max_length=100, default="default value")
    description = models.CharField(max_length=100, default="default value")
    unit = models.CharField(max_length=100, default="default value")
    dimensions = models.FloatField(default=0.0) 
    weight = models.FloatField(default=0.0)
    brand = models.CharField(max_length=100, default="default value")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    area = models.FloatField()
    capacity = models.IntegerField()
    openingtime = models.TimeField()
    closingtime = models.TimeField()
    type = models.CharField(max_length=10,default="default value")

class Stock(models.Model):
    name = models.CharField(max_length=100, default="default value")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='stock')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='stock')
    quantity = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="stock", null=True, blank=True, default=None)

    class Meta:
        unique_together = (('item', 'warehouse'),)

class Packaging(models.Model):
    type = models.CharField(max_length=100, default="returnable")  
    item = models.ForeignKey(Item, on_delete=models.CASCADE,unique=True) 
    quantity = models.IntegerField(default=0)
    weight = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    capacity = models.FloatField(default=0.0)
    dimensions = models.FloatField(default=0.0)
    unit = models.CharField(max_length=100, default="")
    storagespace = models.FloatField(default=0.0)

class Sales(models.Model):
    amount = models.FloatField()
    date = models.DateField()
    currency = models.CharField(max_length=50, default="default value")
    payment_method = models.CharField(max_length=50, default="default value")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="sales", unique=True)
    quantity = models.IntegerField()

class Purchase(models.Model):
    amount = models.FloatField()
    date = models.DateField()
    currency = models.CharField(max_length=50, default="default value")
    payment_method = models.CharField(max_length=50, default="default value")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="purchase", unique=True)
    quantity = models.IntegerField()

class Payment(models.Model):
    amount = models.FloatField()
    date = models.DateField()
    currency = models.CharField(max_length=50, default="default value")
    payment_method = models.CharField(max_length=50, default="default value")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="payment", unique=True)
    quantity = models.IntegerField()


class PackagingMouvment(models.Model):
    name = models.CharField(max_length=100, default="default value")
    packaging = models.ForeignKey(Packaging, related_name='mouvment', on_delete=models.CASCADE,default="no notes ")
    mouvement = models.CharField(max_length=100, default="default value")
    issue_fee = models.FloatField(default=0.0)
    issue_bill = models.FloatField(default=0.0)


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    packaging = models.ForeignKey(Packaging, related_name='orders', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name="orders", on_delete=models.CASCADE)
    order_date = models.DateField(default="default value")
    notes = models.CharField(max_length=100, default="no notes ")
    item_price = models.FloatField()
    returnablepackage_price = models.FloatField()
    status = models.CharField(max_length=10, default='Pending')
    order_number = models.CharField(max_length=20, default="unknown order")
    shipping_address = models.CharField(max_length=30, default="self pickup")
    total_amount = models.FloatField()
    payment_method = models.CharField(max_length=20, default="cash")

    class Meta:
        unique_together = ('packaging', 'item')


class Shipment(models.Model):
    packaging = models.OneToOneField(Packaging, on_delete=models.CASCADE, unique=True, related_name="shipment")
    tracking_number = models.CharField(max_length=100, default="default value")
    status = models.CharField(max_length=100, default="default value")










