# Condicional IF
color = input("Ingrese color preferido: ")
if color == "rojo":
    print("El color es rojo.")
else:
    print("El color es diferente de rojo.")

# Operadores de comparacion

"""
Operadores de comparacion
== : igual a
!= : diferente a
<, >, <=, >= : para valores numericos
"""

ing_valor = input("Ingrese valor numerico: ")
valor = int(ing_valor)

if valor > 100:
    print(f"El valor {str(valor)} es muy grande")

if valor != 7:
    print(f"{str(valor)} es un numero corriente")
else:
    print("Es tu dia de suerte")

# IF anidado

pais = input("Pais en el que resides: ")
ciudad = input("Ciudad del pais en el que te encuentras: ")

if pais == "Ecuador":
    if ciudad == "Guayaquil":
        print(f"Vives en {pais} y en la ciudad de {ciudad}")
    else:
        print(f"Vives en {pais} y en otra ciudad de ese pais")
else:
    print("Vives en un pais diferente al que observas")

# ELIF

tienes_perro = input("Tienes perro (S/N)? ")
if tienes_perro == "S":
    raza = input("Raza del perro: ")
    if raza == "salchicha":
        print("Es salchicha")
    elif raza == "pastor aleman":
        print("Es pastor aleman")
    else:
        print("Raza desconocida")
else:
    print("No tiene perro")

"""
Operadores logicos
and :  y
or : o
not : negacion
"""

i_edad = input("Ingrese edad: ")
limite = 65
edad = int(i_edad)

if edad < 25:
    print("La edad actual supone no ser adultez plena")
elif edad >= 25 and edad < 65:
    print("Edad de desempeño en trabajo y formacion familiar")
else:
    print("Pertenece a la jubilacion")

booleano = True
print("Cambio el valor de booleano a:",not booleano)
