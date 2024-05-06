from rest_framework import serializers
from product_api.models import Product, Order, OrderDetail

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Product model.

    This serializer is used to convert the Product model instances into JSON
    representations and vice versa. It specifies the fields that should be
    included in the serialized output.

    Attributes:
        model (class): The model class that the serializer should be based on.
        fields (list): The fields that should be included in the serialized output.
    """

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock']



class OrderDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for the OrderDetail model.

    This serializer is used to convert the OrderDetail model instances into JSON
    representation and vice versa. It specifies the fields that should be included
    in the serialized output.

    Attributes:
        model (OrderDetail): The model class that this serializer is associated with.
        fields (list): The fields to be included in the serialized output.

    """

    class Meta:
        model = OrderDetail
        fields = ['id', 'order_id', 'quantity', 'product_id']


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Order model.
    """

    order_details = OrderDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'date', 'client', 'order_details']
