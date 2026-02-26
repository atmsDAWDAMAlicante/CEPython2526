
from datetime import date, timedelta, datetime
from Vista.Entradas import Introducciones
from Modelo.Validaciones import Validaciones

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_productos = []

        # Atributos fecha, igual que los trabajadores

        fecha = "2024-01-01"
        try:
            fecha_OK = datetime.strptime(fecha, "%Y-%m-%d").date()
            self.fecha_alta = fecha_OK
        except ValueError:
            self.fecha_alta = date.today()
        self.fecha_baja = None

    def realizar_pedido(self):
        pass

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
            fecha_provisional = Introducciones.reiterar_entrada("Introduce correctamente una fecha válida (aaaa-mm-dd)")
            posible_fecha = Validaciones.validar_fecha(fecha_provisional)
        else:
            self.fecha_baja = posible_fecha
            print(f' La fecha de baja es: {self.fecha_baja}')

    def antiguedad(self):
        try: 
            (self.fecha_baja - self.fecha_alta).days
        except Exception:
            print("Verifique que se han introducido correctamente las fechas de alta y baja")
            print(self.__dict__)
        else:
            return (self.fecha_baja - self.fecha_alta).days