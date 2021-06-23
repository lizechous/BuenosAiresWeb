from rest_framework import serializers
from .models import BodegaProducto

class BodegaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodegaProducto
        fields = '__all__'
