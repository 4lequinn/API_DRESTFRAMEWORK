# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agencia(models.Model):
    id_agencia = models.IntegerField(primary_key=True)
    nom_agencia = models.CharField(max_length=35, blank=True, null=True)
    pct_agencia = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agencia'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nom_categoria = models.CharField(max_length=20)
    pct = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class Consumo(models.Model):
    id_consumo = models.IntegerField(primary_key=True)
    id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='id_reserva')
    id_huesped = models.ForeignKey('Huesped', models.DO_NOTHING, db_column='id_huesped')
    monto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'consumo'


class DetalleReserva(models.Model):
    id_reserva = models.OneToOneField('Reserva', models.DO_NOTHING, db_column='id_reserva', primary_key=True)
    id_habitacion = models.ForeignKey('Habitacion', models.DO_NOTHING, db_column='id_habitacion')

    class Meta:
        managed = False
        db_table = 'detalle_reserva'
        unique_together = (('id_reserva', 'id_habitacion'),)


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
    id = models.BigAutoField(primary_key=True)
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


class Empleado(models.Model):
    run_empleado = models.CharField(primary_key=True, max_length=10)
    nom_empleado = models.CharField(max_length=40)
    dir_empleado = models.CharField(max_length=60)
    fono_empleado = models.IntegerField()
    sueldo_base = models.IntegerField()
    comision = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria')
    run_supervisor = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class Empleados(models.Model):
    legajo = models.IntegerField(primary_key=True)
    documento = models.CharField(max_length=8)
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=30, blank=True, null=True)
    sueldo = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    hijos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleados'


class EncData(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    enc_psw = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'enc_data'


class ErroresProceso(models.Model):
    id_error = models.FloatField(primary_key=True)
    nomsubprograma = models.CharField(max_length=200)
    msg_error = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'errores_proceso'


class Habitacion(models.Model):
    id_habitacion = models.IntegerField(primary_key=True)
    tipo_habitacion = models.CharField(max_length=2)
    valor_habitacion = models.IntegerField()
    valor_minibar = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'habitacion'


class Huesped(models.Model):
    id_huesped = models.IntegerField(primary_key=True)
    appat_huesped = models.CharField(max_length=25)
    apmat_huesped = models.CharField(max_length=25)
    nom_huesped = models.CharField(max_length=24)
    id_procedencia = models.ForeignKey('Procedencia', models.DO_NOTHING, db_column='id_procedencia', blank=True, null=True)
    id_agencia = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='id_agencia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'huesped'


class HuespedTour(models.Model):
    id_huespedtour = models.IntegerField(primary_key=True)
    id_huesped = models.ForeignKey(Huesped, models.DO_NOTHING, db_column='id_huesped')
    id_tour = models.ForeignKey('Tour', models.DO_NOTHING, db_column='id_tour')
    num_personas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'huesped_tour'


class Libros(models.Model):
    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=20, blank=True, null=True)
    editorial = models.CharField(max_length=20, blank=True, null=True)
    edicion = models.DateField(blank=True, null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'libros'


class Procedencia(models.Model):
    id_procedencia = models.IntegerField(primary_key=True)
    nom_procedencia = models.CharField(max_length=70)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')

    class Meta:
        managed = False
        db_table = 'procedencia'


class RangosConsumos(models.Model):
    id_tramo = models.FloatField(primary_key=True)
    vmin_tramo = models.FloatField(blank=True, null=True)
    vmax_tramo = models.FloatField(blank=True, null=True)
    pct = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rangos_consumos'


class Region(models.Model):
    id_region = models.BooleanField(primary_key=True)
    nom_region = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'region'


class Reserva(models.Model):
    id_reserva = models.IntegerField(primary_key=True)
    id_huesped = models.ForeignKey(Huesped, models.DO_NOTHING, db_column='id_huesped')
    ingreso = models.DateField()
    estadia = models.IntegerField()
    run_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='run_empleado')

    class Meta:
        managed = False
        db_table = 'reserva'


class SalidasDiariasHuespedes(models.Model):
    id_huesped = models.IntegerField()
    nombre = models.CharField(max_length=60)
    alojamiento = models.IntegerField()
    consumos = models.IntegerField()
    tours = models.IntegerField()
    subtotal_pago = models.IntegerField()
    descuento_consumos = models.IntegerField()
    descuentos_procedencia = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'salidas_diarias_huespedes'


class Supervisor(models.Model):
    run_supervisor = models.OneToOneField(Empleado, models.DO_NOTHING, db_column='run_supervisor', primary_key=True)
    empleados = models.FloatField(blank=True, null=True)
    bono_responsabilidad = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supervisor'


class TotalConsumos(models.Model):
    id_huesped = models.IntegerField(primary_key=True)
    monto_consumos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'total_consumos'


class Tour(models.Model):
    id_tour = models.FloatField(primary_key=True)
    nom_tour = models.CharField(max_length=50)
    valor_tour = models.IntegerField()
    tiempo = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tour'


class Usuarios(models.Model):
    nombre = models.CharField(max_length=10, blank=True, null=True)
    clave = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
