"""
Bucle FOR:
for var in elemento_iter (lista, rango, etc)
    bloq_instrucciones

NOTA: el espaciado (4 caracteres) delimita el nivel, por lo que eso evita el
uso de corchetes
"""

i = 0
for i in range(0,9): # equivale al generico for(i=0; i<9; i++)
    print("i = ", i)

i = 0
numero = 1
for i in range(0,9):
    print("i = ", i)
    numero *= 10
    print("numero = ", numero)

print("==================Tabla de multiplicar==================")
num = int(input("Tabla de multiplicar del "))
if num < 1:
    num = 1
for i in range(1,13):
    print(f"{num} x {i} = {num*i} ")
else: # condicion cuando no cumple el bucle
    print("=======================================================")

print("=======================================================")

print("\nProlongacion de numero...")
num2 = int(input("Ingrese un valor limite menor de 10 para visualizar numeros: "))
if num2 < 1:
    num2 = 1
i = 0
if num2 >= 10:
    print("Valor no permitido")
else:
    for i in range (1,100):
        num2 += 1
        if num2 >= 10:
            break
        i *= num2
        print("num2: ", num2)
    else:
        print("Bucle finalizado")


