from django import forms
from django.forms import ModelForm, fields, widgets
from .models import BodegaProducto, SolicitudServicio

class BodegaProductoForm(ModelForm):
    class Meta:
        model = BodegaProducto
        fields = [ 'id_producto', 'nombre_producto', 'descripcion', 'marca', 'precio', 'en_stock']

        labels = {
            'id_producto': 'ID Producto',
            'nombre_producto': 'Nombre producto',
            'descripcion': 'Descripcion',
            'marca': 'Marca',
            # 'fecha_creacion': 'Fecha ',
            'precio': 'Precio',
            'en_stock': 'En stock',
        }
        
        widgets = {
            'id_producto': forms.TextInput(attrs={'class': 'form-control'}), 
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'en_stock' : forms.TextInput(attrs={'class': 'form-control'}),
        }
        


class SolicitudServicioForm(ModelForm):
    class Meta:
        model = SolicitudServicio
        fields = ['id_solicitud','s_rut', 's_telefono', 's_correo', 's_tipo_servicio', 'fecha_visita', 'descripcion_req']

        labels = {
            
            'id_solicitud': 'ID Solicitud',
            's_rut': 'Rut',
            's_telefono': 'Teléfono',
            's_correo': 'Correo electrónico',
            's_tipo_servicio': 'Tipo de servicio',
            # 'fecha_creacion': 'Fecha ',
            'fecha_visita': 'Fecha de visita',
            'descripcion_req': 'Descripción',
            # 'estado_ss' : "Estado",
        }

        widgets = {
            'id_solicitud': forms.TextInput(attrs={'class': 'form-control'}),
            's_rut': forms.Select(attrs={'class': 'form-control'}), 
            's_telefono': forms.TextInput(attrs={'class': 'form-control'}),
            's_correo': forms.TextInput(attrs={'class': 'form-control'}),
            's_tipo_servicio': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_visita' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_req' : forms.TextInput(attrs={'class': 'form-control'}),
            # 'estado_ss' : forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class SolicitudServicioAgendaForm(ModelForm):
    class Meta:
        model = SolicitudServicio
        fields = ['id_solicitud','id_tec', 'rut_tecnico', 'acepta_fecha_visita', 'fecha_visita_tec', 'estado_ss']

        labels = {
            
            'id_solicitud': 'ID Solicitud',
            'id_tec': 'ID Tecnico',
            'rut_tecnico': 'Rut tecnico',
            'acepta_fecha_visita': 'Acepta fecha visita',
            'fecha_visita_tec': 'Fecha de visita',
            # 'fecha_creacion': 'Fecha ',
            'estado_ss': 'Estado solicitud',
           
        }

        widgets = {
            'id_solicitud': forms.TextInput(attrs={'class': 'form-control'}),
            'id_tec': forms.Select(attrs={'class': 'form-control'}), 
            'rut_tecnico': forms.TextInput(attrs={'class': 'form-control'}),
            'acepta_fecha_visita': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_visita_tec': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_ss' : forms.TextInput(attrs={'class': 'form-control'}),
            
        }