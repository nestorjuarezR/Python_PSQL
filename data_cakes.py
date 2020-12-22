import psycopg2

TABLE_CAKE = ''' CREATE TABLE pasteles(
    id SERIAL,
    cliente VARCHAR(80), 
    sabor VARCHAR(80),
    tamaño VARCHAR(80),
    color VARCHAR(80)
    )'''

def add_order():
    cliente = input('Ingrese el nombre del cliente: ')
    sabor = input('Ingrese el sabor del pastel: ')
    tamaño = input('Ingrese el tamaño del pastel: ')
    color = input('Ingrese el color de betun del pastel: ')
    
    return cliente,sabor,tamaño, color

def update_order():
    id_order = int(input("Ingrese el id del usuario que desea actualizar: "))
    cliente = input('Ingrese el nombre del cliente: ')
    sabor = input("Ingrese el nuevo sabor del pastel: ")
    tamaño = input("Ingrese el tamaño del pastel: ")
    color = input('Ingrese el nuevo color de betun del pastel: ')

    return cliente, sabor, tamaño, color, id_order


print('''
<---------->
Bienvenido
<---------->

- Seleccione una opción:
1.- Agregar Orden
2.- Mostrar Ordenes
3.- Eliminar Orden
4.- Actualizar Orden
5.- Salir
''' )

sql_add_order = "INSERT INTO pasteles (cliente,sabor,tamaño,color) VALUES(%s,%s,%s,%s)"
sql_show = "SELECT * FROM pasteles"
sql_delete = "DELETE FROM pasteles WHERE id=%s"
sql_update = "UPDATE pasteles SET cliente=%s sabor=%s tamaño=%s color=%s WHERE id=%s"

def menu():
    connection = psycopg2.connect(
    host = 'localhost',
    user = 'nestorjr',
    password = '123456',
    dbname = 'pasteles')
    print('<----- Conexion exitosa ----->')

    opcion = int(input('Ingrese el numero de la opcion seleccionada: '))
    with connection.cursor() as cursor:
        if opcion == 1:
            cursor.execute(sql_add_order, add_order())
            connection.commit()
        if opcion == 2:
            cursor.execute(sql_show)
            for order in cursor.fetchall():
                print(order)

menu()