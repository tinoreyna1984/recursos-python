"""
Escribir un programa que aniada valores a una lista
mientras que la longitud de esta sea menor a 120
"""

from random import random


lista = []
cont = 0

while len(lista) < 120:
    i = int(random()*100)
    lista.append(i)
    print("Valor aniadido a lista: ", i)
    cont += 1
else:
    print(f"Llegamos a los {cont} elementos")
print(lista)

lista = []
for j in range(1,121):
    i = int(random()*100)
    lista.append(i)
    print("Valor aniadido a lista: ", i)
else:
    print(f"Llegamos a los {len(lista)} elementos")
print(lista)


