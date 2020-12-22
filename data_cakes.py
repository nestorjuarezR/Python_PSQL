import psycopg2

TABLE_CAKE = ''' CREATE TABLE pasteles(
    id SERIAL,
    cliente VARCHAR(80), 
    sabor VARCHAR(80),
    tamaño VARCHAR(80),
    color VARCHAR(80)
    )'''

def presentation():
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

def add_order():
    cliente = input('Ingrese el nombre del cliente: ')
    sabor = input('Ingrese el sabor del pastel: ')
    tamaño = input('Ingrese el tamaño del pastel: ')
    color = input('Ingrese el color de betun del pastel: ')
    
    return cliente,sabor,tamaño, color

def update_order():
    id_order = int(input('Ingrese el id del usuario que desea actualizar: '))
    cliente = input('Ingrese el nombre del cliente: ')
    sabor = input('Ingrese el nuevo sabor del pastel: ')
    tamaño = input('Ingrese el tamaño del pastel: ')
    color = input('Ingrese el nuevo color de betun del pastel: ')

    return cliente, sabor, tamaño, color, id_order


#def back_menu():
#    back_decision = str(input('¿Desea realizar otra accion (S/N)? '))
#    if back_decision == 'S' or 's':
#        presentation()
#        menu()
#    elif back_decision == 'N' or 'n':
#        exit
#    else:
#        print('Ingrese una opcion valida !!!')


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
            print('Orden Registrada con exito')
            #back_menu()
            
        elif opcion == 2:
            cursor.execute(sql_show)
            for order in cursor.fetchall():
                print(order)
            #back_menu()

        elif opcion == 3:
            decision = str(input('Desea obtener el listado de Ordenes? (S/N): '))
            if decision == 'S' or 's':
                cursor.execute(sql_show)
                for order in cursor.fetchall():
                    print(order)
                
            elif decision == 'N' or 'n':
                pass
                
            id_order = int(input('Ingrese el numero de orden a eliminar: '))   
            cursor.execute(sql_delete,(id_order,))
            connection.commit()
            print('Orden eliminada con exito !!!')
            #back_menu()
            
        elif opcion == 4:
            cursor.execute(sql_show)
            for order in cursor.fetchall():
                print(order)
            cursor.execute(sql_update, update_order())
            connection.commit()
            print('Orden actualizada con exito !!!')
            #back_menu()
        
        elif opcion == 5:
            exit
        
        else:
            print('Ingrese una opcion valida !!!')
            presentation()
            menu()

    connection.close()

presentation()
menu()