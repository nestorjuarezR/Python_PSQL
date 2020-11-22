import psycopg2

try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'nestorjr',
        password = '123456',
        dbname = 'test')
    print('<----- Conexion exitosa ----->')
    cursor = connection.cursor()
    connection.close()

except psycopg2.Error as error:
    print('Error con la conexion !!!', error)