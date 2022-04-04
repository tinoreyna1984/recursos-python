# conexion a una base de datos SQLite

# importar modulo
import sqlite3

# conexion

#abrir
conexion = sqlite3.connect('pruebas.db')

# crear cursor
cursor = conexion.cursor()

# crear tabla

sql = (
    'CREATE TABLE IF NOT EXISTS productos('
    'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL'
    ', titulo varchar(255)'
    ', descripcion text'
    ', precio int(255)'
    ')'
)
cursor.execute(sql)

# guardar cambios
conexion.commit()

#cerrar
conexion.close()
