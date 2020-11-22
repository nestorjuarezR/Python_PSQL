import psycopg2


try:
    psycopg2.connect(
        host = 'localhost',
        user = 'nestorjr',
        password = '123456',
        dbname = 'test')
    print('<----- Conexion exitosa ----->')

    5/0
except psycopg2.Error as error:
    print('Error con la conexion !!!', error)
except Exception as e:
    print('Error general:', e)


