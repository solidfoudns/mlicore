__author__ = 'seader'
from rest_framework import serializers
from ecomerce.orders.models import Orden, OrderItem


class OrdenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orden
        fields = ( 'nombre', 'apellidos','email', 'direccion', 'codigo_postal', 'ciudad', 'pagado')


# class OrderItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderItem
#         fields = ( 'orden', 'product', 'precio', 'cantidad')
#