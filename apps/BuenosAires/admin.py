from apps.BuenosAires.models import MaestroUsuario
from django.contrib import admin
from .models import BodegaProducto, BodegaStock, MaestroUsuario
# Register your models here.
admin.site.register(MaestroUsuario)
admin.site.register(BodegaProducto)
admin.site.register(BodegaStock)