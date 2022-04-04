"""
Listas en Python: arreglos/arrays
"""

# se definen de dos formas
ciudades_peru = ["Lima", "Cusco", "Arequipa"]
ciudades_ecuador = list(("Quito", "Guayaquil", "Cuenca"))

print(ciudades_peru)
print(ciudades_ecuador)
print(type(ciudades_peru))
print(type(ciudades_ecuador))

numeros = list(range(1,10))
print(numeros)
print(type(numeros))

de_todo = ['hola', 2, None]
print(de_todo)

# indices

nums_txt = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
print(nums_txt[0]) # primer elemento desde el inicio
print(nums_txt[-1]) # primer elemento desde el final
print(nums_txt[2:5]) # elementos 2 al 4 (siempre es una posicion antes del segundo valor)
print(nums_txt[2:]) # elementos desde posicion 2
print(nums_txt[:5]) # elementos hasta la posicion 4 (siempre es una posicion antes del segundo valor)
print(nums_txt.index("tres")) # devuelve la posicion del elemento "tres"


nums_txt = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
print(nums_txt)
nums_txt[1] = "menos dos"
print(nums_txt) # reemplaza "dos" por "menos dos"

# agregar o quitar elementos de lista
genero_musical = ['rock', 'pop', 'salsa', 'merengue', 'reggaeton', 'bolero', 'cumbia', 'clasico']
print(genero_musical)
genero_musical.remove('reggaeton') # quito 'reggaeton' de la lista de generos musicales
print(genero_musical)
genero_musical.append('vallenato') # agrego 'vallenato' a la lista
print(genero_musical)

# recorrer una lista
print("\n\n\n=======================")
print("Lista de 3 peliculas")
print("=======================")

i = 0
pelis = []
while i < 3:
    peli = input("Ingrese pelicula: ")
    pelis.append(peli)
    i += 1
for peli in pelis:
    print(f"{pelis.index(peli)+1}: {peli}")




