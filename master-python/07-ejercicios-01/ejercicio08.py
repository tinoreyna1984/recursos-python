"""
De dos numeros ingresados, obtener el porcentaje de uno de ellos respecto del otro
"""

numero = int(input("Ingrese numero inicial: "))
prct = int(input("Ingrese porcentaje deseado: "))

print(f"El {prct}% de {numero} es {float(prct*numero/100)}")



