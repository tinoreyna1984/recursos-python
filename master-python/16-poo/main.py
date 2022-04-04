#  importo clase

from clases import *

# creo una instancia de Vehiculo
carrito = Terrestre('rojo', 4, 120)

if(carrito.esCarro()):
    print("Es carro")

print(type(carrito)) # tipado de la instancia carrito
print(isinstance(carrito, Terrestre)) # carrito pertenece a la clase Terrestre?
print(issubclass(Terrestre,Vehiculo)) # Terrestre pertenece a la clase Vehiculo

tren = Tren('rojo',0,200,"A1")
tren.infoTren()