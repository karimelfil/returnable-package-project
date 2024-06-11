from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Warehouse)
admin.site.register(Stock)
admin.site.register(Sales)
admin.site.register(Purchase)
admin.site.register(Payment)
admin.site.register(Packaging)
admin.site.register(Order)