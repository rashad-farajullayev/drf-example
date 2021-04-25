from rest_framework import serializers
from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "customer_id", "order_date", "total_amount", "discount", "paid_amount", "change_amount")


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    product_id = serializers.IntegerField()
    order_id = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ("quantity", "product_id", "product", "order_id")


class OrderDetailsSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(read_only=True)
    orderitem_set = OrderItemSerializer(many=True)
    customer_id = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ("id", "customer_id", "customer", "order_date", "total_amount",
                  "discount", "paid_amount", "change_amount", "orderitem_set")
        depth=1

    def create(self, validated_data):
        order_items = validated_data.pop('orderitem_set')
        order = Order.objects.create(**validated_data)
        for oi in order_items:
            oi['order_id'] = order.id
            OrderItemSerializer(oi).create(oi)

        return order


