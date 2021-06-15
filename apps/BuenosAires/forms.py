from django import forms
from .models import BuenosAires, MaestroUsuario


class RecetaForm(forms.ModelForm):
    class Meta:
        model = MaestroUsuario
        fields = ['id_usuario', 'contrasena', 'rut_usuario', 'tipo_usuario', 'nombre', 'correo']
        labels = {
            'id_usuario': 'Id usuario',
            'contrasena': 'Constraseña',
            'rut_usuario': 'Rut usuario',
            'tipo_usuario': 'Tipo de usuario',
            'nombre': 'Nombre',
            'correo': 'Correo'
            

        }
        widgets = {
            'id_usuario': forms.NumberInput(attrs={'class': 'form-control'}),
            'contrasena': forms.TextInput(attrs={'class': 'form-control'}),
            'rut_usuario': forms.TextInput(attrs={'class': 'form-control', 'maxlength' : '12'}),
            'tipo_usuario': forms.Select(choices="TIPO_USUARIO", attrs={'class':'form-control'}),
            'nombre': forms.Textarea(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}), 
        }
