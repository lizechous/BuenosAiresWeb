from django import forms
from django.forms import ModelForm, fields
from .models import BodegaProducto

class BodegaProductoForm(ModelForm):
    class Meta:
        model = BodegaProducto
        fields = [ 'id_producto', 'nombre_producto', 'descripcion', 'marca', 'precio', 'en_stock']


