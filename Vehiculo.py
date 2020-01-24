class Vehiculo():
    def __init__(self, marca, modelo, precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio
        self.__comision = 0

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo
    
    def getPrecio(self):
        return self.__precio

    def getComision(self):
        self.__comision = self.__precio * 0.02
        return self.__comision