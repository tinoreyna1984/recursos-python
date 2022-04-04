'''
Uso de try-except: similar al try-catch de otros lenguajes para manejo de
errores/excepciones
'''

try: # instruccion a probar
    nombre = input("Ingresa tu nombre: ")
    if(len(nombre) > 0):
        nom_user = "Mi nombre es " + nombre
    print(nom_user)
except: # ocurre algun error inesperado
    print("Error de valor")
else: # cuando la instruccion funciona correctamente
    print("Correcto.")
finally: # instruccion que se ejecutara siempre
    print("Completada la instruccion")





