from Venta import Venta
from Vehiculo import Vehiculo
from Archivo import Archivo
from MongoDB import Mongo
from pymongo import MongoClient

class Menu():
    def __init__(self):
        self.__venta = Venta()
        self.__db = Mongo()
    
    def pVenta(self):
        return input('¿Agregar un automóvil? (s/n): ')

    def pEmpleado(self):
        return input('¿Deseas agregar un empleado? (s/n): ')
    
    def nuevoEmpleado(self):
        nombre = input('Ingresa el nombre del empleado: ')
        self.__venta.nuevoEmpleado(nombre)
        # Insertar Empleado a la base de datos (recive al objeto empleado)
        self.__db.insertarEmpleado(self.__venta.getEmpleado())
        self.nuevoVehiculo()

    
    def qNuevoEmpleado(self):
        respuesta = self.pEmpleado()
        while not respuesta == 'n':
            self.nuevoEmpleado()
            respuesta = self.pEmpleado()

    def nuevoVehiculo(self):
        respuesta = self.pVenta()
        while not respuesta == 'n':
            marca = input('Ingresa la marca: ')
            modelo = input('Ingresa el modelo: ')
            precio = float(input('Ingresa el precio: '))
            v = Vehiculo(marca, modelo, precio)
            self.__venta.getEmpleado().addVehiculo(v)
            # Insertar Auto a la base de datos (recive al objeto auto , bono del empleado, comisiones empleado)
            self.__db.insertarAuto(v , self.__venta.getEmpleado().getBono(), self.__venta.getEmpleado().getComisiones())
            respuesta = self.pVenta()
        self.__venta.guardarEmpleado()
        self.imprimirEmpleado()

    def imprimirVehiculos(self):
        for vehiculo in self.__venta.getEmpleado().getvVendidos():
            print(vehiculo.getModelo())

    def imprimirEmpleado(self):
        print('---------------------')
        print("Nombre: " + self.__venta.getEmpleado().getNombre() + " Salario: " + str(self.__venta.getEmpleado().getSalario()) + " Comision: " + str(self.__venta.getEmpleado().getComisiones()))
        print('---------------------')

    def imprimirEmpleados(self):
        print('---------------------')
        print('\x1b[6;30;42m' + 'Lista de Empleados' + '\x1b[0m')

        for empleado in self.__venta.getEmpleados():
            print("Nombre: " + empleado.getNombre() + " Salario: "  + str(empleado.getSalario()) + " Comisiones: " + str(empleado.getComisiones()))
    
    def imprimirNomina(self):
        print('---------------------')
        print('Nomina: ${0}'.format(self.__venta.getNomina()))

    def cargarArchivo(self):
        respuesta = input('¿Deseas cargar el archivo? (s/n): ')
        if(respuesta == 's'):
            archivo = Archivo()
            self.__venta.setEmpleados(archivo.cargarLista())
    
    def guardarArchivo(self, empleados):
        respuesta = input('¿Deseas guardar el archivo? (s/n): ')
        if(respuesta == 's'):
            archivo = Archivo()
            archivo.guardarLista(empleados)
            self.imprimirEmpleados()


    def run(self):
        # self.cargarArchivo()
        self.qNuevoEmpleado()
        self.imprimirEmpleados()
        self.imprimirNomina()
        # self.guardarArchivo(self.__venta.getEmpleados())