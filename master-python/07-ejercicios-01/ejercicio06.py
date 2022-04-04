"""
Mostrar tablas de multiplicar del 1 al 10.
Mostrar el titulo y las multiplicaciones del 1 al 10
"""

i = 1
j = 1

for i in range(1,11):
    print("========================================")
    print(f"Tabla del {i}")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
print("========================================")

