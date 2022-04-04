# Funciones predefinidas

# type
print(type("hola"))
print(type(2))

# isinstance
print(isinstance("hola",int))

# Funciones con cadenas

print("   hola ".strip()) # limpia espacios
print(len("burro")) # longitud de cadena

frase = "Lo que he escrito, he escrito"
print(frase.find("he")) # encuentra la posicion donde ocurre la 1a palabra o frase en texto (desde cero)

texto = "El tiempo lo cura todo"
print(texto.replace("tiempo","amor")) # reemplaza la(s) palabra(s) halladas en texto por una nueva

texto = "tino"
print(texto.upper()) # pone el texto en mayusculas
texto = "TINO"
print(texto.lower()) # pone el texto en minusculas
print(texto.capitalize()) # capitaliza el texto
