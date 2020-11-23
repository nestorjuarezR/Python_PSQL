import psycopg2
import hashlib
import getpass

TABLE_CAKE = ''' CREATE TABLE pasteles(
    id SERIAL,
    cliente VARCHAR(80), 
    sabor VARCHAR(80),
    tamaño VARCHAR(80),
    color VARCHAR(80)
    )'''

#print('''
#<---------->
#Bienvenido
#<---------->
#
#- Seleccione una opción:
#1.- Agregar Orden
#2.- Mostrar Ordenes
#3.- Eliminar Orden
#4.- Actualizar Orden
#5.- Salir
#''' )


def add_order():
    cliente = input('Ingrese el nombre del Cliente: ')
    sabor = input('Ingrese el sabor del pastel: ')
    tamaño = input('Ingrese el tamaño del pastel: ')
    color = input('Ingrese el color del betun: ')
    
    return cliente,sabor,tamaño,color

try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'nestorjr',
        password = '123456',
        dbname = 'pasteles')
    print('<----- Conexion exitosa ----->')
    
    sql_add_order = "INSERT INTO pasteles (cliente,sabor,tamaño,color) VALUES(%s,%s,%s,%s)"

    with connection.cursor() as cursor:
        #cursor.execute(TABLE_CAKE)        #CREA LA TABLA
        cursor.execute(sql_add_order, add_order())          #Agrega nueva orden
        connection.commit()
        connection.close()

except psycopg2.Error as error:
    print('Error con la conexion !!!', error)