# Importamos la librería para conectarnos a ORACLE
from django.db import connections

'''
def uwu():
    cursor = connections['default'].cursor()
    #empleados = cursor.execute("select * from empleado")
    call = cursor.connection.cursor()
    out = cursor.connection.cursor()
    #call.close()
    #print('Se cerró la conexión')
    #call.callproc("SP_LISTAR_EMPLEADOS",[out])

    #lista = []

    #for fila in out:
        #print(fila)
    
    a = call.execute("select * from empleado")
    for x in a:
        print(x)
'''

'''
try:
    connection = cx_Oracle.connect(
        user = 'p3liss',
        password = 'p3liss',
        dsn = '127.0.0.1:1521/orcl',
        encoding = 'UTF-8'
    )
    # print(connection.version)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM empleado")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print('Conexión finalizada')


'''

def listarEmpleados():
    lista = []
    try:
        cursor = connections['default'].cursor()
        out = cursor.connection.cursor()

        # Hacemos la llamada al SP
        cursor.callproc('SP_LISTAR_EMPLEADOS',[out])

        for x in out:
            lista.append(x)
            print(x)    

    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        out.close()
        print('Cerró la conexión')
        return lista