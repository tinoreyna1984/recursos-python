# agregar o quitar elementos de lista
genero_musical = ['rock', 'pop', 'salsa', 'merengue', 'reggaeton', 'bolero', 'cumbia', 'clasico']

print(genero_musical)
genero_musical.remove('reggaeton') # quito 'reggaeton' de la lista de generos musicales
print(genero_musical)
genero_musical.append('vallenato') # agrego 'vallenato' a la lista
print(genero_musical)
genero_musical.pop(6) # elimino el elemento en la posicion 6 ("clasico")
print(genero_musical)
genero_musical.insert(3, "funk") # agrego "funk" en la posicion 3 de la lista
print(genero_musical)

# reordenamiento
numeros = list((1,40,20,3,4,5,10,2,50,100))
print(numeros)
numeros.sort() # ordena los numeros
print(numeros)
numeros.reverse() # invierte el orden de los numeros
print(numeros)

# validar existencia de item en lista
print("salsa" in genero_musical) # devuelve True
print(5 in numeros) # devuelve True
print("metal" in genero_musical) # devuelve False

# cantidad de elementos en un arreglo
print(len(genero_musical))

# cantidad de veces que aparece un elemento en lista
lista = [1,2,3,4,1,5,6,7,8, "a", "b", "c", "a"]
print(lista.count(2)) # 2 aparece 1 vez
print(lista.count(1)) # 1 aparece 2 veces
print(lista.count("a")) # "a" aparece 2 veces
print(lista.count("c")) # "c" aparece 1 vez

# unir dos listas
lista_uno = [1,2,3,4,5]
lista_dos = [6,7,8,9,10]
print(lista_uno)
print(lista_dos)
lista_uno.extend(lista_dos)
print(lista_uno)




