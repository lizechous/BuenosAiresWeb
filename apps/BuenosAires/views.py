from django.shortcuts import render, redirect, get_object_or_404
from .models import BodegaProducto
from django.views.generic import ListView

# IMPORTACIONES API
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BodegaProductoSerializer
# from django.shortcuts import render, redirect, get_object_or_404


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
