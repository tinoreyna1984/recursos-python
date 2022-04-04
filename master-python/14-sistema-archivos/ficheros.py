'''
Sistema de archivos
'''

# Crea archivo
#archivo = open('f_texto.txt', 'w')

# Crea y abre el archivo
archivo = open('f_texto.txt', 'a+')

# Escribe en archivo
archivo.write('hola, soy un fichero en Python\n')

# Cerrar archivo
archivo.close()

# Abre archivo para lectura
archivo = open('f_texto.txt', 'r')
#print(archivo.read())

for elemento in archivo.readlines():
    print(elemento)

'''
Operaciones con archivos
* rutas del archivo: ruta/archivo.ext
import shutil
import os
Copiar: shutil.copyfile(string_ruta_antigua, string_ruta_nueva)
Mover/renombrar: shutil.move(string_ruta_antigua, string_ruta_nueva)
Eliminar: os.remove(string_ruta_archivo)
'''
