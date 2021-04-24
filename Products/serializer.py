from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ("id", "name", "description", "ean", "price", "prod_date", "exp_date")
