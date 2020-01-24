from Venta import Venta
from Archivo import Archivo

class Menu():
    def __init__(self):
        self.__venta = Venta()
    
    def pVenta(self):
        return input('¿Agregar un automóvil? (s/n): ')

    def pEmpleado(self):
        return input('¿Deseas agregar un empleado? (s/n): ')
    
    def nuevoEmpleado(self):
        nombre = input('Ingresa el nombre del empleado: ')
        self.__venta.nuevoEmpleado(nombre)
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
            self.__venta.getEmpleado().addVehiculo(marca, modelo, precio)
            respuesta = self.pVenta()
        self.__venta.guardarEmpleado()
        self.imprimirEmpleado()
        self.qNuevoEmpleado()

    def imprimirVehiculos(self):
        for vehiculo in self.__venta.getEmpleado().getvVendidos():
            print(vehiculo.getModelo())

    def imprimirEmpleado(self):
        print('---------------------')
        print("Nombre: " + self.__venta.getEmpleado().getNombre() + " Salario: " + str(self.__venta.getEmpleado().getSalario()) + " Comision: " + str(self.__venta.getEmpleado().getComisiones()))
        print('---------------------')

    def imprimirEmpleados(self):
        print('---------------------')
        print('Lista de empleados:')

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
        self.cargarArchivo()
        self.qNuevoEmpleado()
        self.imprimirEmpleados()
        self.imprimirNomina()
        self.guardarArchivo(self.__venta.getEmpleados())