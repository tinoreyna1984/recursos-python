'''
Uso de clases
'''

class Vehiculo():

    # la buena practica ensenia que los atributos deben ser privados
    # y solo sean accesible por los metodos publicos de la clase (encapsulamiento)
    # El caracter "__" privatiza el atributo de clase
    

    __color = ''
    __ruedas = 0
    __velocidad = 0

    # constructor
    def __init__(self, color, ruedas, velocidad):
        self.__color = color
        self.__ruedas = ruedas
        self.__velocidad = velocidad
    
    def acelerar(self, velocidad):
        self.__velocidad += velocidad

    def getColor(self):
        return self.__color
    
    def getVelocidad(self):
        return self.__velocidad

    def getRuedas(self):
        return self.__ruedas
    
    def setColor(self, color):
        self.__color = color
    
    def setVelocidad(self, velocidad):
        self.__velocidad = velocidad

    def setRuedas(self, ruedas):
        self.__ruedas = ruedas

# Terrestre es una subclase de Vehiculo (herencia)
class Terrestre(Vehiculo):

    # super invoca al constructor de la clase padre
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas, velocidad)

    # se aplica el uso del metodo publico para acceder a un atributo privado
    def esCarro(self):
        if self.getRuedas() == 4:
            return True
        else:
            return False

class Ferroviaria():
    
    __ruta = ''

    # constructor
    def __init__(self,ruta):
        self.__ruta = ruta

    def setRuta(self, ruta):
        self.__ruta = ruta

    def getRuta(self):
        return self.__ruta

# herencia multiple
class Tren(Terrestre, Ferroviaria):

    def __init__(self, color, ruedas, velocidad, ruta):
        super().setColor(color)
        super().setRuedas(ruedas)
        super().setVelocidad(velocidad)
        super().setRuta(ruta)

    def infoTren(self):
        print("Info del tren: ")
        print("- Ruedas vehiculares corrientes: " + str(self.getRuedas()))
        print("- Color: " + self.getColor())
        print("- Velocidad promedio: " + str(self.getVelocidad()))
        print("- Consultar por rutas de forma independiente.")

