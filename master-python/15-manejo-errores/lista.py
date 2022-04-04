lista = [1,2,3,5,10,2,11,6]

try:
    num = int(input("Ingrese valor de la lista a buscar: "))
    for item in lista:
        if num in lista:
            print("Se encontro valor ingresado")
            break
except ValueError as err:
    print("Valor no valido")
finally:
    print('Fin de la prueba')
