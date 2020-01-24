from Vehiculo import Vehiculo

class Empleado():
    def __init__(self, nombre, salario = 500):
        self.__nombre = nombre
        self.__salario = salario 
        self.__vVendidos = []
        self.__comisiones = 0

    def getNombre(self):
        return self.__nombre

    def getSalario(self):
        return self.__salario
    
    def getComisiones(self):
        return self.__comisiones
    
    def getvVendidos(self):
        return self.__vVendidos
    
    def addVehiculo(self, marca, modelo, precio):
        v = Vehiculo(marca, modelo, precio)
        self.__comisiones += v.getComision()
        self.__salario += 1000
        self.__vVendidos.append(v)