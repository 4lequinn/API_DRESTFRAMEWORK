from rest_framework.response import Response
from rest_framework.views import APIView
from apps.empleados.models import *
from apps.empleados.api.serializers import EmpleadoSerializer, Empleado2Serializer


from apps.empleados.oracle_conection import *  

# Haremos lo mismo pero con un decorador
from rest_framework.decorators import api_view


class EmpleadoAPIView(APIView):
    # Recibimos peticiones GET
    def get(self,request):
        empleados = Empleado.objects.all()
        empleados_serializers = EmpleadoSerializer(empleados, many=True) # Le indicamos que le enviamos un listado
        return Response(empleados_serializers.data)


@api_view(['GET','POST'])
def empleado_api_view(request):
    if request.method == 'GET':
        empleados = Empleado.objects.all()
        empleados_serializers = EmpleadoSerializer(empleados, many=True) # Le indicamos que le enviamos un listado
        print(len(listarEmpleados()))        
        return Response(empleados_serializers.data)

    elif request.method == 'POST':
        empleados_serializers = EmpleadoSerializer(data = request.data)
        if empleados_serializers.is_valid():
            empleados_serializers.save()
            return Response(empleados_serializers.data)
        return Response(empleados_serializers.errors)


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
            print(data)
            lista.append(data)

        results = Empleado2Serializer(lista,many=True).data
        return Response(results)