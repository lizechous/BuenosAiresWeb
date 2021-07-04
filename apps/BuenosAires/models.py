# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Banco(models.Model):
    id_banco = models.IntegerField(primary_key=True)
    nombre_banco = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco'


class BodegaDespacho(models.Model):
    id_od = models.IntegerField(primary_key=True)
    id_factura = models.ForeignKey('WebFacturaVenta', models.DO_NOTHING, db_column='id_factura', blank=True, null=True)
    estado_od = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bodega_despacho'


class BodegaProducto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=60, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    marca = models.CharField(max_length=30, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    en_stock = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bodega_producto'


class BodegaStock(models.Model):
    id_producto = models.ForeignKey(BodegaProducto, models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    nombre_producto = models.CharField(max_length=60, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bodega_stock'


class DetalleFacturaVenta(models.Model):
    id_producto = models.ForeignKey(BodegaProducto, models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    id_factura = models.ForeignKey('WebFacturaVenta', models.DO_NOTHING, db_column='id_factura', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    precio_unitario = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_factura_venta'
        
    
            


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MaestroCliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=12)
    nombre_cli = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maestro_cliente'

TIPO_USUARIO = (
    ('Tecnico', 'Tecnico'),
    ('Vendedor', 'Vendedor'),
    ('Bodeguero', 'Bodeguero'),
)

class MaestroUsuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    contrasena = models.CharField(max_length=20, blank=True, null=True)
    rut_usuario = models.CharField(max_length=12, blank=True, null=True)
    tipo_usuario = models.CharField(max_length=30, blank=True, null=True, choices=TIPO_USUARIO)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maestro_usuario'


class SolicitudServicio(models.Model):
    id_solicitud = models.IntegerField(primary_key=True)
    s_rut = models.ForeignKey(MaestroCliente, models.DO_NOTHING, db_column='s_rut', blank=True, null=True)
    s_telefono = models.IntegerField(blank=True, null=True)
    s_correo = models.CharField(max_length=50, blank=True, null=True)
    s_tipo_servicio = models.CharField(max_length=10, blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)
    fecha_visita = models.DateField(blank=True, null=True)
    descripcion_req = models.CharField(max_length=300, blank=True, null=True)
    id_tec = models.ForeignKey(MaestroUsuario, models.DO_NOTHING, db_column='id_tec', blank=True, null=True)
    rut_tecnico = models.CharField(max_length=12, blank=True, null=True)
    acepta_fecha_visita = models.CharField(max_length=1, blank=True, null=True)
    fecha_visita_tec = models.DateField(blank=True, null=True)
    estado_ss = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitud_servicio'


class TablaTarjeta(models.Model):
    id_banco = models.ForeignKey(Banco, models.DO_NOTHING, db_column='id_banco', blank=True, null=True)
    num_cuenta_bancaria = models.BigIntegerField(primary_key=True)
    tipo_cuenta = models.CharField(max_length=10, blank=True, null=True)
    c_rut = models.ForeignKey(MaestroCliente, models.DO_NOTHING, db_column='c_rut', blank=True, null=True)
    saldo_disponible = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tabla_tarjeta'


class WebFacturaVenta(models.Model):
    id_factura = models.IntegerField(primary_key=True)
    rut_cli = models.ForeignKey(MaestroCliente, models.DO_NOTHING, db_column='rut_cli', blank=True, null=True)
    tipo_factura = models.CharField(max_length=30, blank=True, null=True)
    fecha_emision = models.DateField(blank=True, null=True)
    fecha_despacho = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    valor_total = models.FloatField(blank=True, null=True)
    direccion_envio = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_factura_venta'
        
    
    
        
