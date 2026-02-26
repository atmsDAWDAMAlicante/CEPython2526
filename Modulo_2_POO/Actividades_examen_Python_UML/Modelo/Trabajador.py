from abc import ABC, abstractmethod # En el diagrama de clases del enunciado hay una CLASE ABSTRACTA llamada interfaz
from datetime import date, timedelta, datetime
from Vista.Entradas import Introducciones
from Modelo.Validaciones import Validaciones


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
        self.password = "1Ab"
        
        fecha = "2024-01-01"
        try:
            fecha_OK = datetime.strptime(fecha, "%Y-%m-%d").date()
            self.fecha_alta = fecha_OK
        except ValueError:
            self.fecha_alta = date.today()
        self.fecha_baja = None


    # GETTERS Y SETTERS de los dos atributos privados del diagrama de clases del enunciado
    
    def get_dni(self):
        return self.__dni
    def set_dni(self, dni):
        self.__dni = dni

    def get_sueldo(self):
        return self.__sueldo
    def set_sueldo(self, sueldo):
        self.__sueldo = sueldo


    # Métodos de la clase abstracta
    def dar_de_alta(self):
        fecha_provisional = Introducciones.introducir_fecha()
        posible_fecha = Validaciones.validar_fecha(fecha_provisional)
        while (posible_fecha == False):
            fecha_provisional = Introducciones.reiterar_entrada("Introduce correctamente una fecha válida (aaaa-mm-dd): ")
            posible_fecha = Validaciones.validar_fecha(fecha_provisional)
        else:
            self.fecha_alta = posible_fecha
            print(f' La fecha de alta es: {self.fecha_alta}')
    def dar_de_baja(self):
        fecha_provisional = Introducciones.introducir_fecha()
        posible_fecha = Validaciones.validar_fecha(fecha_provisional)
        while (posible_fecha == False):
            fecha_provisional = Introducciones.reiterar_entrada("Introduce correctamente una fecha válida (aaaa-mm-dd): ")
            posible_fecha = Validaciones.validar_fecha(fecha_provisional)
        else:
            self.fecha_baja = posible_fecha
            print(f' La fecha de baja es: {self.fecha_baja}')

    def antiguedad(self):
        try: 
            (self.fecha_baja - self.fecha_alta).days
        except Exception:
            print("Verifique que se han introducido correctamente las fechas de alta y baja.")
            print(self.__dict__)
        else:
            return (self.fecha_baja - self.fecha_alta).days
    


