"""
Crear un programa que compruebe que un texto este vacio, lo rellene con letras y
las capitalice
"""

texto = " "

if len(texto.strip()) <= 0:
    texto = "hola mundo"
    print(texto.capitalize())

