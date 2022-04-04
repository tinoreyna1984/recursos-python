'''
Directorios
'''

import os

# Crear y borrar directorios
if not os.path.isdir('./dir_prueba'):
    os.mkdir('./dir_prueba')
else:
    os.rmdir('./dir_prueba')

# Listar directorio
print(os.listdir('./'))
