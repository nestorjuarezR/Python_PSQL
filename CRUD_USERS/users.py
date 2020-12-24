import hashlib
from db import connection
import getpass

class User:
    def __init__(self, name, age, password):
        self.__name = name
        self.__age = age
        self.__password = password

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
    
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    name = property(get_name, set_name)
    age = property(get_age, set_age)
    password = property(get_password, set_password)

    def __str__(self):
        return "Usuario: {}".format(self.name)

class UserMethods:

    @classmethod
    def create_user(cls):
        name = input('Ingrese el nombre del usuario: ')
        age = int(input('Ingrese la edad: '))
        password = getpass.getpass('Ingrese su contraseña: ')
        user = User(name, age, password)
        return user



    @classmethod
    def set_password(cls, password):
        password = hashlib.sha256(password.encode()).hexdigest()
        return password


class UserDB:

    @classmethod
    def insert_user(cls, user, cursor):
        name = user.name
        age = user.age
        password = UserMethods.set_password(user.password)
        query = "INSERT INTO users(name, age , password) VALUES(%s, %s , %s)"
        cursor.execute(query, (name, age, password))
        print('\nUsuario registrado con exito\n')
        cursor.close()

    @classmethod
    def delete_user(cls, cursor):
        id_user = int(input('Ingrese el ID del usuario a eliminar: '))
        query =  "SELECT id FROM users WHERE id = %s"
        cursor.execute(query, (id_user,))
        user = cursor.fetchone()
        if user:
            query = "DELETE FROM users WHERE id = %s"
            cursor.execute(query, (id_user,))
            print('Usuario eliminado con exito')
        else:
            print('El id que ingreso no existe en la base de datos')
        cursor.close()


    @classmethod
    def list_users(cls,cursor):
        query = "SELECT id, name, age FROM users"
        cursor.execute(query)
        print('<----- Usuarios Registrados ----->')
        for id, name, age in cursor.fetchall():
            print('| ID: {} | Nombre: {} | Edad: {} |'.format(id, name, age))
        cursor.close()


    @classmethod
    def update_user(cls, cursor):
        id_user = int(input('Ingrese el ID del usuario para actualizar: '))
        query =  "SELECT id FROM users WHERE id = %s"
        cursor.execute(query, (id_user,))
        user = cursor.fetchone()
        if user:
            name = input('Ingrese el nuevo nombre del usuario: ')
            age = int(input('Ingrese la edad del usuario: '))
            password = UserMethods.set_password(getpass.getpass('Ingrese la nueva contraseña del usuario: '))
            query = "UPDATE users  SET name = '{}', age = {}, password = '{}' WHERE id = {}".format(name, age, password, id_user)
            cursor.execute(query)
            print('-> Usuario Actualizado con exito')
        else:
            print('Ingrese un ID valido')
        cursor.close()