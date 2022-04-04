"""
Mostrar todos los numeros impares habidos entre dos numeros ingresados por el usuario
"""

num01 = int(input("Ingrese primer numero: "))
num02 = int(input("Ingrese segundo numero: "))

i = num01

if num01 < num02:
    for i in range(num01,num02+1):
        if i % 2 != 0:
            print("Valor impar actual: ", i)
        i += 1
    else:
        print("Fin")



