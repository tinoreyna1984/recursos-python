"""
Crear una lista de 8 numeros.
Hacer una funcion que recorra listas de numeros y devuelva un string
Ordenarla y mostrarla
Mostrar su longitud
Buscar un elemento que el usuario pida por teclado
"""

lista = [1,2,3,5,10,2,11,6]
print(lista)

for item in lista:
    print(f"Item actual: ", item)

lista.sort()
print(lista)
print(len(lista))

def genera_string(lista):
    cadena = ""
    for item in lista:
        if lista.index(item) < len(lista) - 1:
            cadena = cadena + str(item) + "-"
        else:
            cadena = cadena + str(item)
    return cadena

print(genera_string(lista))

num = int(input("Ingrese valor de la lista a buscar: "))
for item in lista:
    if num in lista:
        print("Se encontro valor ingresado")
        break



