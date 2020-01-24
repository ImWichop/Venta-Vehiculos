import pickle

class Archivo():
    def __init__(self):
        self.__empleados = []

    def guardarLista(self, empleados):
        print('\x1b[6;30;42m' + 'Menú de Reportes' + '\x1b[0m')
        print('1) Guardar reporte')
        print('2) Salir')
        option = input('Selecciona la opción que desees: ')

        if(option == '1'):
            fichero_binario = open("lista_ventas","wb")
            pickle.dump(empleados, fichero_binario)
            fichero_binario.close()
            del(fichero_binario)

    def cargarLista(self):
        fichero = open("lista_ventas", "rb")
        self.__empleados = pickle.load(fichero)
        
        return self.__empleados