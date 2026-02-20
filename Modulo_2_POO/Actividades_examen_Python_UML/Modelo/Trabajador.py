from abc import ABC, abstractmethod # ESTO ES PORQUE EN EL DIAGRAMA DE CLASES HAY UNA CLASE ABSTRACTA LLAMADA INTERFAZ




# CLASE TRABAJADOR:
    # CLASE ABSTRACTA ESTADO (interfaz)
    # CLASES HIJAS CAMARERO Y COCINERO


class Estado(ABC): # CLASE ABSTRACTA (INTERFAZ)
    @abstractmethod
    def dar_de_alta(self):
        pass
    def dar_de_baja(self):
        pass


class Trabajador(Estado): # CLASE PADRE DE CAMARERO Y COCINERO 
    _id_autoincremental = 0 # ATRIBUTO DE CLASE CON UNA _ porque pone el diagrama que es PROTECTED (Java)
    # ESTE ATRIBUTO LO HEREDARÁN TODOS LOS TRABAJADORES, PERO SOLO SE USARÁ EN EL CONSTRUCTOR DE LA CLASE TRABAJADOR PARA ASIGNAR EL ID AUTOINCREMENTAL A CADA TRABAJADOR
    def __init__ (self, nombre, dni, sueldo):
        self.nombre = nombre
        self.__dni = dni
        self.__sueldo = sueldo
        Trabajador._id_autoincremental += 1
        self._id = Trabajador._id_autoincremental
        


    # GETTERS Y SETTERS
    
    def get_dni(self):
        return self.__dni
    def set_dni(self, dni):
        self.__dni = dni

    def get_sueldo(self):
        return self.__sueldo
    def set_sueld(self, sueldo):
        self.__sueldo = sueldo



    
    # MÉTODOS DE LA CLASE ABSTRACTA ESTADO (INTERFAZ)
    def dar_de_alta(self):
        pass
    def dar_de_baja(self):
        pass


