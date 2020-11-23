import psycopg2
import hashlib
import getpass

TABLE_USER = ''' CREATE TABLE users(
    id SERIAL, 
    name VARCHAR(20),
    age SMALLINT,
    password VARCHAR(80)
    )'''


def get_user_from_terminal_insert():
    name = input("Ingrese su Nombre: ")
    age = int(input("Ingrese su edad: "))
    password = getpass.getpass("Ingrese su contraseña: ")
    password = hashlib.sha256(password.encode()).hexdigest()      #Cifrado password
    
    return name, age , password

def get_user_from_terminal_update():
    id_user = int(input("Ingrese el id del usuario que desea actualizar: "))
    name = input("Ingrese el nuevo Nombre: ")
    age = int(input("Ingrese la nueva edad: "))
    password = getpass.getpass("Ingrese la nueva contraseña: ")
    password = hashlib.sha256(password.encode()).hexdigest()      #Cifrado password
    
    return name, age , password, id_user

try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'nestorjr',
        password = '123456',
        dbname = 'test')
    print('<----- Conexion exitosa ----->')

    sql_insert = "INSERT INTO users (name, age, password) VALUES(%s, %s, %s)"
    sql_select = "SELECT * FROM users"  #SELECT name, age, password
    sql_update = "UPDATE users SET  name=%s, age=%s, password=%s WHERE id=%s"


    with connection.cursor() as cursor:
        #cursor.execute(TABLE_USER)
        #cursor.execute(sql, get_user_from_terminal())
        #connection.commit()
        #print(' <-- Usuario registrado con exito -->')
        print('<-- Usuarios sin modificacion -->')
        cursor.execute(sql_select)
        for user in cursor.fetchall():
            print(user)
        cursor.execute(sql_update, get_user_from_terminal_update())
        connection.commit()

        print('<-- Usuarios actualizados -->')
        cursor.execute(sql_select )
        for user in cursor.fetchall():
            print(user)

    connection.close()

except psycopg2.Error as error:
    print('Error con la conexion !!!', error)