from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        models = Order
        fields = [
            'client_type',
            'order_status',
            'name',
            'phone',
            'address',
            'room',
            'entrance',
            'floor',
            'delivery_price',
            'discount_sum',
            'pay_id',
            'margin_order',
            'persons',
            'pre_order',
            'comment',
            'staff_comment',
            'created_at',
            'updated_at',
        ]
