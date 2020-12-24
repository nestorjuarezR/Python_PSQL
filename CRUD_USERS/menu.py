from db import connection
from users import UserDB, UserMethods


def select_option(con, option):
    with con.cursor() as cursor:

        if option == 1:
            user = UserMethods.create_user()
            UserDB.insert_user(user, cursor)
        elif option == 2:
            UserDB.delete_user(cursor)
        elif option == 3:
            UserDB.list_users(cursor)
        elif option == 4:
            UserDB.update_user(cursor)
        else:
            print('\n Ingrese una opcion valida !!!\n')
        con.commit()


def menu():
    menu = '''
    1.- Agregar Usuario\n
    2.- Eliminar Usuario\n
    3.- Listar Usuarios\n
    4.- Actualizar Usuarios\n
    5.- Salir\n
    -> Opcion: '''
    con = connection()
    while True:
        option = int(input(menu))
        if option == 5:
            break 
        select_option(con,option)

menu()