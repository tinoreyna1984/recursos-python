'''
Multiples errores
'''

def division(a, b):
    return a/b

# NameError -> variable no definida
# ZeroDivisionError -> division entre cero
# TypeError -> tipo de dato no soportado (se uso tipos no validos como string y None)

try:
    print(division(2,0))
except NameError as n_err:
    print("Variable no definida: " + str(type(n_err)))
except ZeroDivisionError as z_err:
    print("No se puede dividir por cero: " + str(type(z_err)))
except TypeError as t_err:
    print("Tipo de dato en parametro no valido: " + str(type(t_err)))
finally:
    print("Finalizado")
