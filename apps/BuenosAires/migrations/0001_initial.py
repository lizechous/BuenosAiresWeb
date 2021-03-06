# Generated by Django 3.2.4 on 2021-06-15 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('codename', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id_banco', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_banco', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'banco',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BodegaDespacho',
            fields=[
                ('id_od', models.IntegerField(primary_key=True, serialize=False)),
                ('estado_od', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'bodega_despacho',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BodegaProducto',
            fields=[
                ('id_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(blank=True, max_length=60, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('marca', models.CharField(blank=True, max_length=30, null=True)),
                ('precio', models.FloatField(blank=True, null=True)),
                ('en_stock', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'bodega_producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BodegaStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(blank=True, max_length=60, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bodega_stock',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleFacturaVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('precio_unitario', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'detalle_factura_venta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(blank=True, max_length=200, null=True)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField(blank=True, null=True)),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MaestroCliente',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre_cli', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion', models.CharField(blank=True, max_length=30, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('correo', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'maestro_cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MaestroUsuario',
            fields=[
                ('id_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('contrasena', models.CharField(blank=True, max_length=20, null=True)),
                ('rut_usuario', models.CharField(blank=True, max_length=12, null=True)),
                ('tipo_usuario', models.CharField(blank=True, choices=[('Tecnico', 'Tecnico'), ('Vendedor', 'Vendedor'), ('Bodeguero', 'Bodeguero')], max_length=30, null=True)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('correo', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'maestro_usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SolicitudServicio',
            fields=[
                ('id_solicitud', models.IntegerField(primary_key=True, serialize=False)),
                ('s_telefono', models.IntegerField(blank=True, null=True)),
                ('s_correo', models.CharField(blank=True, max_length=50, null=True)),
                ('s_tipo_servicio', models.CharField(blank=True, max_length=10, null=True)),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('fecha_visita', models.DateField(blank=True, null=True)),
                ('descripcion_req', models.CharField(blank=True, max_length=300, null=True)),
                ('rut_tecnico', models.CharField(blank=True, max_length=12, null=True)),
                ('acepta_fecha_visita', models.CharField(blank=True, max_length=1, null=True)),
                ('fecha_visita_tec', models.DateField(blank=True, null=True)),
                ('estado_ss', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'solicitud_servicio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TablaTarjeta',
            fields=[
                ('num_cuenta_bancaria', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tipo_cuenta', models.CharField(blank=True, max_length=10, null=True)),
                ('saldo_disponible', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tabla_tarjeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WebFacturaVenta',
            fields=[
                ('id_factura', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo_factura', models.CharField(blank=True, max_length=30, null=True)),
                ('fecha_emision', models.DateField(blank=True, null=True)),
                ('fecha_despacho', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=30, null=True)),
                ('valor_total', models.FloatField(blank=True, null=True)),
                ('direccion_envio', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'web_factura_venta',
                'managed': False,
            },
        ),
    ]
