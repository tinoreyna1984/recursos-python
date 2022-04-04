"""
Funciones en Python:

def nombre_funcion(args):
    # instrucciones
"""

def suma(a, b):
    return a+b

suma_ = suma(2,3)

print(suma_)

def tabla_mult(num):
    i = 1
    print(f"Tabla del {num}")
    for j in range(1,11):
        print(f"{num} x {i} = {num*i}")
        i += 1

valor = int(input("Ingrese valor para tabla de multiplicar: "))
tabla_mult(valor)


# Parametros opcionales o por defecto

def mi_nombre(nombre = "Tino"):
    print(f"Mi nombre es {nombre}")
mi_nombre()




