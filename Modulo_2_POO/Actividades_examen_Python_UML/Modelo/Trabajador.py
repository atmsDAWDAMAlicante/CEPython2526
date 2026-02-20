from abc import ABC, abstractmethod # En el diagrama de clases del enunciado hay una CLASE ABSTRACTA llamada interfaz




# Clase Trabajador:
    # Hereda de la clase abstracta Estado (interfaz)
    # Clases hijas: Camarero y Cocinero


class Estado(ABC): # Clase abstracta (interfaz en el diagrama de clases)
    @abstractmethod
    def dar_de_alta(self):
        pass
    def dar_de_baja(self):
        pass


class Trabajador(Estado): # Hereda de la clase abstracta Estado

    # Atributo de clase: se le pone una '_'. En el diagrama de clases del enunciado aparece como "protected" 
    _id_autoincremental = 0 # Este atributo lo heredarán todas las clases hijas
    # Pero sólo se ejecutará en el constructor de la clase Trabajador
    # Asigna un id que se autoincrementa
    def __init__ (self, nombre, dni, sueldo):
        self.nombre = nombre
        self.__dni = dni # privado en el diagrama de clases del enunciado
        self.__sueldo = sueldo # privado en el diagrama de clases del enunciado
        Trabajador._id_autoincremental += 1 # 1º se incrementa
        self._id = Trabajador._id_autoincremental # 2º se asigna
        


    # GETTERS Y SETTERS de los dos atributos privados del diagrama de clases del enunciado
    
    def get_dni(self):
        return self.__dni
    def set_dni(self, dni):
        self.__dni = dni

    def get_sueldo(self):
        return self.__sueldo
    def set_sueld(self, sueldo):
        self.__sueldo = sueldo


    # Métodos de la clase abstracta
    def dar_de_alta(self):
        pass
    def dar_de_baja(self):
        pass


