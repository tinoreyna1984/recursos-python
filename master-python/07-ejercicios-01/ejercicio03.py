"""
Mostrar los cuadrados de los primeros 60 numeros naturales.
Programar con for y con while
"""

i = 0
for i in range(0,61):
    print("Numero par actual: ", pow(i,2))
    i += 1
else:
    print("Fin del bucle for")

i = 0
while i < 61:
    print("Numero par actual: ", pow(i,2))
    i += 1
else:
    print("Fin del bucle while")

