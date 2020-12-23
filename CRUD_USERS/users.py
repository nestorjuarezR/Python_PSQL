import hashlib
from db import connection
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
    def set_password(cls, password):
        password = hashlib.sha256(password.encode()).hexdigest()
        return password


class UserDB:

    @classmethod
    def insert_user(cls,user, cursor):
        name = user.name
        age = user.age
        password = UserMethods.set_password(user.password)
        query = "INSERT INTO users(name, age , password) VALUES(%s, %s , %s)"
        cursor.execute(query, (name,age,password))
        print('Usuario registrado con exito')
        cursor.close()

con = connection()
cursor = con.cursor()

nes = User('Nes', 24, '12345')
UserDB.insert_user(nes, cursor)
con.commit()
con.close()


#nes = User('Nes', 24, UserMethods.set_password('12345'))
#print(nes.password)
#nes = User('Nes', 24, '12345')
#print(nes)
#
#majo = User('Maria Jose', 24, '12345')
#print(majo)

