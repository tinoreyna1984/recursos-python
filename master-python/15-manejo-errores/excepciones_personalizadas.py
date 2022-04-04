'''
Excepciones personalizadas.
Lanzar excepciones.
'''

from logging import raiseExceptions

# Los errores/excepciones personalizados/as se definen como clases
class CondError(Exception):
    pass

try:
    num = int(input("Ingrese numero mayor a 4 y menor a 8: "))
    if num > 4 and num < 8:
        print("Numero: ", num)
    else:
        raise CondError('no se cumple la condicion indicada en try')
except ValueError as v_err:
    print("Valor no permitido: " + str(v_err.args[0]))
except CondError as c_err:
    print("No cumple la condicion: " + str(c_err.args[0]))
    raise
finally:
    print("Completado")



