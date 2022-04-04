"""
Tipos de datos
"""

# tipo None
nada = None
print(type(nada))
print(nada)

# otros tipos

entero = 120
print(type(entero))
print(entero)

cadena = "Esta es una cadena"
print(type(cadena))
print(cadena)

dec = 2.3
print(type(dec))
print(dec)

booleano = True
print(type(booleano))
print(booleano)
print(type(not booleano))
print(not booleano)

lista = [1,2,3,10,100,"Tino"]
print(type(lista))
print(lista)

tupla = ("Tino", "Reyna")
print(type(tupla))
print(tupla)

diccionario = {
    "nombre" : "Tino",
    "apellido" : "Reyna",
    "edad" : 37
}
print(type(diccionario))
print(diccionario)

rango = range(9)
print(type(rango))
print(rango)

dato_byte = b"dato byte"
print(type(dato_byte))
print(dato_byte)

# Conversion de un tipo de dato a otro

# numero a texto
edad = 37
print("Tengo",str(edad),"años")

# texto a numero
valor = "85"
print(int(valor)*2)

