# Variables locales y globales

texto = "Soy global"

def funcion():
    #texto = "Soy local" # Si se comenta esta linea, se accede a la variable global (externa a la funcion)
    print(texto)

funcion()

