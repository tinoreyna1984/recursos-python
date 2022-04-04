# Para el caso de MySQL

import mysql.connector

# Crea objeto de conexion
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

# Probar conexion
if database != None:
    print('Conexion correcta')

cursor =  database.cursor()
sql = 'SHOW DATABASES'

cursor.execute(sql)

for bd in cursor:
    print(bd)

'''
Al igual que en el caso anterior con SQLITE, se puede crear las bases de datos, sus tablas
y tambien crear, actualizar y borrar registros:
cursor.execute('CREATE DATABASE esquema_bd') -> crea esquema
y demas instrucciones conocidas en SQL
Terminar siempre con database.commit()
'''


