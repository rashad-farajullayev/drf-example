from django.contrib import admin

# Register your models here.
from Products.models import Products
from Customers.models import Customer
from Orders.models import Order, OrderItem

admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
