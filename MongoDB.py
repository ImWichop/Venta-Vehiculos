from pymongo import MongoClient

class Mongo():
    def __init__(self):
        self.__MONGO_URI = 'mongodb://localhost'
        self.__client = MongoClient(self.__MONGO_URI)
        self.__db = self.__client['ventas']
        self.__cEmpleados = self.__db['empleados']

    def insertarEmpleado(self, empleado):
        self.__cEmpleados.insert_one({
            "_id" : self.__cEmpleados.find().count()+1,
            "nombre" : empleado.getNombre(),
            "salario" : empleado.getSalario(),
            "vVendidos" : [],
            "bono" : empleado.getBono(),
            "comisiones" : empleado.getComisiones()
        })
    
    def insertarAuto(self, auto, bono, comisiones):
        empleado = self.__cEmpleados.find_one({"_id" : self.__cEmpleados.find().count()})
        lista = empleado['vVendidos']
        lista.append({
            "marca" : auto.getMarca(),
            "modelo" : auto.getModelo(),
            "precio" : auto.getPrecio(),
            "comision" : auto.getComision()
        })
        self.__cEmpleados.update_one({"_id" : self.__cEmpleados.find().count()},{"$set" : {"vVendidos" : lista, "bono" : bono, "comisiones" : comisiones}})
