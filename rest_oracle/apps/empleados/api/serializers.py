from rest_framework import serializers
from apps.empleados.models import *

# Creamos las clases para Serializar
# Nos convierte a una estructura de JSON
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'



# Custom Serializer
class Empleado2Serializer(serializers.Serializer):
    run_empleado = serializers.CharField(max_length=10)
    nom_empleado = serializers.CharField(max_length=40)
    dir_empleado = serializers.CharField(max_length=60)
    fono_empleado = serializers.IntegerField()
    sueldo_base = serializers.IntegerField()
    comision = serializers.DecimalField(max_digits=4, decimal_places=2)
    id_categoria = serializers.IntegerField()
    run_supervisor = serializers.CharField(max_length=10)
