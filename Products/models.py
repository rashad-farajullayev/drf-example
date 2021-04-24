from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=2000)
    ean = models.CharField(max_length=50)
    price = models.FloatField()
    prod_date = models.DateField()
    exp_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

