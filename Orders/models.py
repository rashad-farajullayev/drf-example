from django.db import models

from Customers.models import Customer
from Products.models import Products


class Order(models.Model):
    customer = models.ForeignKey(Customer, verbose_name="Customer", on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField()
    total_amount = models.FloatField()
    discount = models.FloatField()
    paid_amount = models.FloatField()
    change_amount = models.FloatField()


class OrderItem(models.Model):
    quantity = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} {self.quantity}"
