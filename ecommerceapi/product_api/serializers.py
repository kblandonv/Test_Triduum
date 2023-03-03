from rest_framework import serializers
from product_api.models import Product, Order, OrderDetail

# Importamos el modelo de Product
# Creamos la clase ProductSerializer
# Indicamos que es un modelo serializador
# Indicamos los campos que queremos serializar

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock']

# Importamos el modelo de Order
# Creamos la clase OrderSerializer
# Indicamos que es un modelo serializador
# Indicamos los campos que queremos serializar

# Importamos el modelo de OrderDetail
# Creamos la clase OrderDetailSerializer
# Indicamos que es un modelo serializador
# Indicamos los campos que queremos serializar

class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = ['id', 'order_id', 'quantity', 'product_id']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
