import psycopg2


def connection():
    try:
        connection = psycopg2.connect(
            host = 'localhost',
            user = 'nestorjr',
            password = '123456',
            dbname = 'test')
        print('''
        <-------------------->
           Conexion Exitosa
        <-------------------->''')
        return connection
    except psycopg2.Error as error:
        print('Error en la conexion:', error)

connection()