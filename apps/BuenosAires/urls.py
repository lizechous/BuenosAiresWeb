from django.urls import path, include
from django.conf.urls import url
from . import views
from apps.BuenosAires.views import bodegaProducto_collection, bodegaProducto_element

urlpatterns = [


       path('api/list_bodega_productos/',  views.bodegaProducto_collection , name='list_bodega_productos'),
       path('api/list_bodega_productos/<int:pk>/', views.bodegaProducto_element ,name='bodega_producto_element')


]
