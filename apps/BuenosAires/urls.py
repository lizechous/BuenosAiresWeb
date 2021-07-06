from django.urls import path, include
from django.conf.urls import url

# from apps.BuenosAires.webpayplus import routes
from . import views 
from apps.BuenosAires.views import bodegaProducto_collection, bodegaProducto_element, Agregar_producto, Lista_productos, Modificar_producto, Eliminar_producto, agregar_producto_carro, eliminar_producto_carro, restar_producto_carro, limpiar_carro, Crear_solicitud, Lista_solicitudes, Eliminar_solicitud, actualizar_stock, Agendar_solicitud, Lista_solicitudes_agendadas, Modificar_estado, Lista_historial_servicios
# from apps.BuenosAires.webpayplus.routes import webpay_plus_create, webpay_plus_commit

# Lista_productos, Modificar_producto, Eliminar_producto
urlpatterns = [

    #------------ PRODUCTOS EN BODEGA BA ---------------
    # Agregar producto BA
    path('shop/agregar_producto', views.Agregar_producto.as_view(), name="agregar_producto"),     

    # Listar productos BA
    path('shop/lista_productos', views.Lista_productos.as_view() , name="lista_productos"),
    
#     # Modificar producto BA
    path('shop/editar_producto/<int:pk>', views.Modificar_producto.as_view(), name='editar_producto'),

#     # Eliminar producto BA
    path('shop/eliminar_producto/<int:pk>', views.Eliminar_producto.as_view(), name='eliminar_producto'),

    # APIS BODEGA BA
    path('api/list_bodega_productos/',  views.bodegaProducto_collection , name='list_bodega_productos'),
    path('api/list_bodega_productos/<int:pk>/', views.bodegaProducto_element ,name='bodega_producto_element'),

    # Listar productos BA tienda 
    
    path('tiendaBA', views.Lista_productos_tienda.as_view(), name='listar_productos_tienda'),
    
    path('agregar/<int:producto_id>', views.agregar_producto_carro , name="agregar"),
    path('eliminar/<int:producto_id>', views.eliminar_producto_carro , name="eliminar"),
    path('restar/<int:producto_id>', views.restar_producto_carro , name="restar"),
    path('limpiar', views.limpiar_carro , name="limpiar"),
    
    # ------------SOLICITUD SERVICIO--------------------------
    path('servicio/crear_solicitud', views.Crear_solicitud.as_view(), name="crear_solicitud"),   
    path('servicio/lista_solicitudes', views.Lista_solicitudes.as_view(), name="lista_solicitudes"),
    path('servicio/eliminar_solicitud/<int:pk>', views.Eliminar_solicitud.as_view(), name='eliminar_solicitud'),
    
    
    path('shop/actualizar_stock/<int:pk>', views.actualizar_stock.as_view(), name='actualizar_stock'),
    
    # --------------------AGENDA SOLICITUDES------------------------------------------------------
    path('servicio/agendar_solicitud/<int:pk>', views.Agendar_solicitud.as_view(), name='agendar_solicitud'),
    path('servicio/lista_solicitudes_agendadas', views.Lista_solicitudes_agendadas.as_view() , name="lista_agenda_solicitudes"),
    path('servicio/modificar_estado/<int:pk>', views.Modificar_estado.as_view(), name='modificar_estado'),
    path('servicio/lista_historial_servicios', views.Lista_historial_servicios.as_view() , name="lista_historial_servicios"),
]
