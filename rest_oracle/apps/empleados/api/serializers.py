from rest_framework import serializers
from apps.empleados.models import *

# Creamos las clases para Serializar
# Nos convierte a una estructura de JSON
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

    # Método que me sirve para representar los datos en un listado
    def to_representation(self,instance):
        #data = super().to_representation(instance)
        return {
           'rut' : instance['run_empleado'],
           'nombre' : instance['nom_empleado']
        }




# Custom Serializer

# Si quiero crear validaciones especificas para Crear o Actualizar debo:
# Gestinarlas en los métodos respectivos según el caso
# O bien crear 1 serializador para cada caso 

class Empleado2Serializer(serializers.Serializer):
    run_empleado = serializers.CharField(max_length=10)
    nom_empleado = serializers.CharField(max_length=40)
    dir_empleado = serializers.CharField(max_length=60)
    fono_empleado = serializers.IntegerField()
    sueldo_base = serializers.IntegerField()
    comision = serializers.DecimalField(max_digits=4, decimal_places=2)
    id_categoria = serializers.IntegerField()
    run_supervisor = serializers.CharField(max_length=10, allow_blank=True, allow_null=True)

    # Validaciones CUSTOM
    # Sobreescribimos los Métodos

    def validate_run_empleado(self,value):
        return value 

    def validate_nom_empleado(self,value):
        # Custom validation
        if 'mona_xina' in value:
            raise serializers.ValidationError('Error el empleado no se puede llamar mona xina')
        return value    

    def validate_dir_empleado(self,value):
        return value
    def validate_fono_empleado(self,value):
        return value
    
    def validate_sueldo_base(self,value):
        return value

    def validate_comision(self,value):
        return value

    def validate_id_categoria(self,value):
        return value

    def validate_run_supervisor(self,value):
        if self.validate_run_empleado(self.context['run_empleado']) == value: #in
            raise serializers.ValidationError('El rut del empleado y el rut del supervisor no pueden ser los mismos')
        return value

    def validate(self,data):
        #if data['run_empleado'] in data['run_supervisor']:
        #    raise serializers.ValidationError('El rut del empleado y el rut del supervisor no pueden ser los mismos')
        print('Validate General')
        return data 

    # Método CREATE en los serializers
    def create(self,validated_data):
        print(validated_data)
        # Le asigno los valores de validated_data
        # Con ** le indicamos que al diccionario, le quite las claves y tome los valores
        # Lo registra en la BDD con la información validada y retorna la instancia
        return Empleado.objects.create(**validated_data)

    def update(self, instance,validated_data):
        # Proceso que hace automáticamente este método
        instance.run_empleado = validated_data.get('run_empleado',instance.run_empleado)
        instance.nom_empleado = validated_data.get('nom_empleado',instance.nom_empleado)
        instance.dir_empleado = validated_data.get('dir_empleado',instance.dir_empleado)
        instance.fono_empleado = validated_data.get('fono_empleado',instance.fono_empleado)
        instance.sueldo_base = validated_data.get('sueldo_base',instance.sueldo_base)
        instance.comision = validated_data.get('comision',instance.comision)
        instance.id_categoria = validated_data.get('id_categoria',instance.id_categoria)
        instance.run_supervisor = validated_data.get('run_supervisor',instance.run_supervisor)
        instance.save()
        return instance


    # Cuando quieres hacer validaciones y no registros en mi base de datos
    '''
    def save(self):
        print(self.validated_data)
        # send_email() Podemos enviar un email
    '''

