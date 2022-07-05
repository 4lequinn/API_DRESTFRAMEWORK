from django.urls import path
#from django.urls import re_path as url
from apps.empleados.api.api import EmpleadoAPIView, empleado_api_view, prueba

urlpatterns = [
    path('empleados/',EmpleadoAPIView.as_view(),name = 'empleado_api'),
    path('empleados2/',empleado_api_view,name = 'empleado_api2'),
    path('prueba/',prueba.as_view(),name = 'prueba'),
]