from django.shortcuts import render, redirect, get_object_or_404
from .models import BodegaProducto
from django.views.generic import ListView

from .forms import BodegaProductoForm


# IMPORTACIONES API
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import BodegaProductoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.db.models import Q 

from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from .serializers import BodegaProductoSerializer
# from django.shortcuts import render, redirect, get_object_or_404



class Agregar_producto(CreateView): 
    model = BodegaProducto 
    form_class = BodegaProductoForm
    template_name = 'bodegaProducto/producto_form.html' 
    success_url = reverse_lazy("agregar_producto") 

class Lista_productos(ListView):
    model = BodegaProducto
    template_name = 'bodegaProducto/lista_productos.html'

# # SE MODIFICA UNA CARRERA 
class Modificar_producto(UpdateView):
    model = BodegaProducto
    form_class = BodegaProductoForm
    template_name = 'bodegaProducto/producto_form.html'
    success_url = reverse_lazy('lista_productos') 

        
class Eliminar_producto(DeleteView):
    model = BodegaProducto
    template_name = 'bodegaProducto/eliminar_producto.html'
    success_url = reverse_lazy('lista_productos')


# APIS 
@api_view(['GET'])
def bodegaProducto_collection(request):
    if request.method == 'GET':
        list = BodegaProducto.objects.all()
        serializer = BodegaProductoSerializer(list, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def bodegaProducto_element(request, pk):
    objeto = get_object_or_404(BodegaProducto, id_producto=pk)

    if request.method == 'GET':
        serializer = BodegaProductoSerializer(objeto)
        return Response(serializer.data)
