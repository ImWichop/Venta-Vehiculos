from Empleado import Empleado

class Venta():
    def __init__(self):
        self.__empleados = []
        self.__empleado = Empleado("")

    def nuevoEmpleado(self, nombre):
        self.__empleado = Empleado(nombre)
    
    def guardarEmpleado(self):
        self.__empleados.append(self.__empleado)
    
    def getNomina(self):
        nomina = 0
        for empleado in self.__empleados:
            nomina += empleado.getSalario()
        return nomina

    def getEmpleados(self):
        return self.__empleados

    def setEmpleados(self, empleados):
        self.__empleados = empleados
    
    def getEmpleado(self):
        return self.__empleado