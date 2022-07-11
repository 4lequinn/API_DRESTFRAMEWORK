from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from apps.empleados.models import *
from apps.empleados.api.serializers import EmpleadoSerializer, Empleado2Serializer


from apps.empleados.oracle_conection import *  

# Haremos lo mismo pero con un decorador
from rest_framework.decorators import api_view


# Visualizar los RESPONSE STATUS
# https://www.django-rest-framework.org/api-guide/status-codes/

class EmpleadoAPIView(APIView):
    # Recibimos peticiones GET
    def get(self,request):
        empleados = Empleado.objects.all().values('run_empleado','nom_empleado')
        empleados_serializers = EmpleadoSerializer(empleados, many=True) # Le indicamos que le enviamos un listado
        return Response(empleados_serializers.data)


@api_view(['GET','POST'])
def empleado_api_view(request):
    if request.method == 'GET':
        empleados = Empleado.objects.all().values('run_empleado', 'nom_empleado')
        empleados_serializers = EmpleadoSerializer(empleados, many=True) # Le indicamos que le enviamos un listado
        print(len(listarEmpleados()))        
        return Response(empleados_serializers.data)

    elif request.method == 'POST':
        empleados_serializers = EmpleadoSerializer(data = request.data)
        if empleados_serializers.is_valid():
            empleados_serializers.save()
            return Response(empleados_serializers.data)
        return Response(empleados_serializers.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def empleado_detail_api_view(request,id = None):
    # Queryset
    empleado = Empleado.objects.filter(run_empleado=id).first()

    # Validación
    if empleado:

        if request.method == 'GET':
            #if run_empleado is not None:
            empleado_serializer = EmpleadoSerializer(empleado).data
            return Response(empleado_serializer, status =  status.HTTP_200_OK)

        elif request.method == 'PUT':
            # request.data aquí viene la información
            empleado_serializer = EmpleadoSerializer(empleado, data = request.data)
            if empleado_serializer.is_valid():
                empleado_serializer.save()
                return Response(empleado_serializer.data)
            return Response(empleado_serializer.errors, status =  status.HTTP_200_OK)

        elif request.method == 'DELETE':
            empleado.delete()
            return Response('Eliminado', status =  status.HTTP_200_OK)
    return Response({'message':'No se ha encontrado el usuario.'},status = status.HTTP_400_BAD_REQUEST)

# Serializador con procedimiento almacenado
class prueba(APIView):
    def get(self, request):
        empleado = listarEmpleados()
        lista = []
        for x in empleado:
            data = {
                'run_empleado' : x[0],
                'nom_empleado' : x[1],
                'dir_empleado' : x[2],
                'fono_empleado' : x[3],
                'sueldo_base' : x[4],
                'comision' : x[5],
                'id_categoria' : x[6],
                'run_supervisor' : x[7]
            }

            lista.append(data)

        results = Empleado2Serializer(lista,many=True).data

        '''
        test_data = {
                'run_empleado' : '20281116-4',
                'nom_empleado' : 'Jorge Mona xina',
                'dir_empleado' : 'XDDD',
                'fono_empleado' : 8738239,
                'sueldo_base' : 283392,
                'comision' : '0.2',
                'id_categoria' : 1,
                'run_supervisor' : None
        }

        validar = Empleado2Serializer(data = test_data, context = test_data)

        if validar.is_valid():
            # Guardar en la base de datos
            validar.save()
            print('Pasó validaciones')
        else:
            print(validar.errors)
        '''
        
        return Response(results, status = status.HTTP_200_OK)