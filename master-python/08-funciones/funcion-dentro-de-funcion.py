# Funciones dentro de funciones

def esto():
    return "Esto"

def esUnTexto():
    return "es un texto"

def muestraTexto():
    texto = f"{esto()} {esUnTexto()}"
    return texto

print(muestraTexto())


