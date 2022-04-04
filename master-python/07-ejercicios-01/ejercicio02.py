"""
Presentar por pantalla los numeros pares del 1 al 120 
"""

i = 0
for i in range(0,121):
    if i % 2 == 0:
        print("Numero par actual: ", i)
    i += 1
else:
    print("Fin del bucle")

