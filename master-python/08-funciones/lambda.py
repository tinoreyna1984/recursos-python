# Funciones lambda
"""
Se emplea para funciones sencillas que no requieran desarrollar con
la instruccion def. En general:
def funcion(args):
    instrucciones
    return retorno
tiene la forma
funcion = lambda args : retorno
"""
def suma(a,b):
    return a+b
print("Suma devuelve: ",suma(2,3))

suma2 = lambda a,b : a+b
print("Suma2 devuelve: ",suma2(2,3))

# suma y suma2 funcionan exactamente igual
