from django.shortcuts import render, redirect, get_object_or_404
from .models import BodegaProducto, SolicitudServicio
from django.views.generic import ListView

from .forms import BodegaProductoForm


# IMPORTACIONES API
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import BodegaProductoForm, SolicitudServicioForm, SolicitudServicioAgendaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.db.models import Q 

from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from .serializers import BodegaProductoSerializer

# IMPORTACION DEL CARRO
from .carro import Carro
# from django.shortcuts import render, redirect, get_object_or_404

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# -----------CRUD PRODUCTOS BA---------------------------------------
class Agregar_producto(CreateView): 
    model = BodegaProducto 
    form_class = BodegaProductoForm
    template_name = 'bodegaProducto/producto_form.html' 
    success_url = reverse_lazy("agregar_producto") 

class Lista_productos(ListView):
    model = BodegaProducto
    template_name = 'bodegaProducto/lista_productos.html'

class Modificar_producto(UpdateView):
    model = BodegaProducto
    form_class = BodegaProductoForm
    template_name = 'bodegaProducto/producto_form.html'
    success_url = reverse_lazy('lista_productos') 

        
class Eliminar_producto(DeleteView):
    model = BodegaProducto
    template_name = 'bodegaProducto/eliminar_producto.html'
    success_url = reverse_lazy('lista_productos')






#------------ APIS ---------------------------------------------------
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
    


#---------------------- TIENDA BA-------------------------------------------

class Lista_productos_tienda(ListView):
    model = BodegaProducto
    template_name = 'bodegaProducto/productos_tienda.html'

class actualizar_stock(DeleteView):
    model = BodegaProducto
    
    template_name = 'bodegaProducto/actualizar_stock.html'
    success_url = reverse_lazy('listar_productos_tienda')  


    
# --------------CARRO --------------------------------------------------------
def agregar_producto_carro(request,producto_id):
    carro = Carro(request)
    producto= BodegaProducto.objects.get(id_producto=producto_id)
    carro.agregar(producto=producto)
    return redirect("listar_productos_tienda")
# # bodegaProducto/listar_productos_tienda
def eliminar_producto_carro (request, producto_id):
    carro = Carro(request)
    producto= BodegaProducto.objects.get(id_producto=producto_id)
    carro.eliminar(producto=producto)
    return redirect("listar_productos_tienda")

def restar_producto_carro (request, producto_id):
    carro = Carro(request)
    producto= BodegaProducto.objects.get(id_producto=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("listar_productos_tienda")

def limpiar_carro (request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("listar_productos_tienda")


# --------------SOLICITUD DE SERVICIO------------------------------------
class Crear_solicitud(CreateView): 
    model = SolicitudServicio
    form_class = SolicitudServicioForm
    template_name = 'bodegaProducto/crear_solicitud_form.html' 
    success_url = reverse_lazy("crear_solicitud") 
    
class Lista_solicitudes(ListView):
    model = SolicitudServicio
    template_name = 'bodegaProducto/lista_solicitudes.html'

class Eliminar_solicitud(DeleteView):
    model = SolicitudServicio
    template_name = 'bodegaProducto/eliminar_solicitud.html'
    success_url = reverse_lazy('lista_solicitudes')
    
class Agendar_solicitud(UpdateView):
    model = SolicitudServicio
    form_class = SolicitudServicioAgendaForm
    template_name = 'bodegaProducto/agenda_solicitud_form.html'
    success_url = reverse_lazy('lista_agenda_solicitudes') 
    
class Lista_solicitudes_agendadas(ListView):
    model = SolicitudServicio
    template_name = 'bodegaProducto/lista_solicitudes_agendadas.html'