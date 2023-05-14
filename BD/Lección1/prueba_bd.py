import psycopg2 # conectar a la base de datos

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db'
                            )
# print(conexion)

cursor = conexion.cursor()
senencia = 'SELECT * FROM persona'
cursor.execute(senencia)
registros = cursor.fetchall() # Recuperar todos los registros de la sentencia
print(registros)

# cerrar la coneión
cursor.close()
conexion.close()